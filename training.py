import random  # Pentru afisarea raspunsurilor din fisierul .json intr-o ordine aleatoare
import json  # Pentru lucrul cu fisiere .json
import pickle
import nltk  # Framework pentru NLP(Natural Language Processing)
import numpy as np

# Pentru eficientizare,vom utilza WordNetLemmatizer,ce ne va permite sa tratam cuvinte asemanatoare ca un singur cuvant (exemplu: munca,munci,munceste-vor fi toate tratate exact la fel)
from nltk.stem import WordNetLemmatizer

# Framework-uri necesare pentru training-ul modelului
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD

# Initializarea constructorului pentru lematizator
lematizator = WordNetLemmatizer()

# Incarcarea fisierului .json
dataset = json.loads(open('intents.json').read())

# Variabile pentru prelucrarea setului de date
clase = []
cuvinte = []
document = []
ignora_literele = ['.', ',', '!', '?']

# Parcurgem fisierul .json,care a fost stocat in variabila dataset sub forma unui dictionar (Python Dictionary)

for i in dataset['intents']:
    for pattern in i['patterns']:
        # Se va obtine o colectie de cuvinte,pentru a diversifica continutul intrebarilor,sau al propozitiilor pe care chatbotul le va primi.In acest fel,nu vor exista posibile diferente intre literele mari si mici,sau intre intrebari si afirmatii.
        lista_cuvinte = nltk.word_tokenize(pattern)
        # Adaugam rezultatul obtinut in lista de cuvinte
        cuvinte.extend(lista_cuvinte)
        document.append((lista_cuvinte, i['tag']))  # Vom separa posibilele intrebari pe care chatbotul le va primi,in functie de un anume tag,care a fost specificat in fisierul .json (ex:pentru propozitiile de intampinare(salut),va exista tag-ul "salutari",pentru intebarile legate de varsta va exista tag-ul "varsta",...,etc.In acest fel,se va face o stratificare cat mai clara a replicilor si intrebarilor,in functie de o anume categorie din care acestea fac parte)
        if i['tag'] not in clase:
            # In situatia in care un anume intent nu se va regasi in lista stocata in variabila clase,o vom adauga ulterior
            clase.append(i['tag'])

# Tratam cuvintele asemanatoare ca un singur cuvant,in situatia in care acestea nu se gasesc in lista literelor ce trebuiesc ignorate
cuvinte = [lematizator.lemmatize(word)
           for word in cuvinte if word not in ignora_literele]
# Eliminam duplicatele
cuvinte = sorted(set(cuvinte))

clase = sorted(set(clase))
# Folosind libray-ul pickle,vom salva in cate un fisier extern toate cuvintele si topic-urile rezultate in urma rularii
pickle.dump(cuvinte, open('cuvinte.pkl', 'wb'))
pickle.dump(clase, open('clase.pkl', 'wb'))

# Utilizam machine learning si retele neuronale pentru implementarea inteligentei artificiale pe care bot-ul o va folosi in comunicarea cu utilizatorul

# Avand in vedere faptul ca aceste retele functioneaza in special cu valori numerice,iar noi pana acum am utilizat exclusiv caractere si siruri si caractere,va trebui sa gasim o conventie de notare a fiecarui cuvant cu 0,sau 1,in functie de pattern-ul pe care utilizatorul il va folosi in comunicarea cu chatbot-ul
training = []
output_gol = [0]*len(clase)

for doc in document:
    # Pentru fiecare valoare din variabila document,vom initializa acest bag de valori numerice,numit container.
    container = []
    pattern_cuvant = doc[0]
    pattern_cuvant = [lematizator.lemmatize(
        word.lower()) for word in pattern_cuvant]
    # Pentru fiecare cuvant din fisierul .json prelucrat care se regaseste in pattern-ul curent,vom atribui container-ului (bag value) valoarea 1.In caz contar,0
    for word in cuvinte:
        container.append(1) if word in pattern_cuvant else container.append(0)

    # Prin copiere,creem o lista de la variabila declarata anterior
    lista_output = list(output_gol)

    lista_output[clase.index(doc[1])] = 1
    training.append([container, lista_output])

random.shuffle(training)
training = np.array(training)
train_x = list(training[:, 0])
train_y = list(training[:, 1])

# Construim neural network-ul

model = Sequential()  # Initializarea modelului,prin utilizarea constructorului.Pentru aceasta etapa,s-au folosit framework-urile tensorflow si keras

# Adaugam layerele
# 1.Layer de input (Dense),ce va contine 128 de neuroni si un input shape dependent de lungimea setului de date antrenat (training)
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)

# Compilarea modelului antrenat
model.compile(loss='categorical_crossentropy',
              optimizer=sgd, metrics=['accuracy'])
# Salvarea locala a acestui model
salvez = model.fit(np.array(train_x), np.array(train_y),
                   epochs=200, batch_size=5, verbose=1)
# Salvarea modelului,cat si a fisierelor binare ce contin informatii referitoare la tag-uri,cat si la propozitiile tokenizate
model.save('chatbot_AI.h5', salvez)
model.save('chatbot_AI.model')

# Afisare mesaj ca urmare a rularii cu succes a aplicatiei
print('Succes!')
