# Proiect-ICDD-Student-s-Helper
Helper pentru studentii Sibieni si nu numai.

# Chatbot-ul Python
Un mic script in Python care implementează funcționalitatea unui chatbot.Folosind Machine Learning, implicit Neural Network si NLP(Neuro-linguistic programming), am reusit sa antrenăm acest mic chatbot,capabil de a purta conversatii in limba romana cu utilizatorul,cat si a face cateva sarcini automatizate pentru acesta.


Nota:Este foarte posibil ca programul sa nu functioneze pe un dispozitiv care nu are instalate framework-urile pe care le-am utilizat in crearea acestui program.Dintre aceste librarii (cele third-party,nespecifice limbajului standard),vom aminti:

-- Keras si TensorFlow  -> Au fost folosite pentru training-ul modelului AI --

-- NLTK  -> s-a folosit pentru NLP (Neuro-linguistic programming) --

-- Pickle -> s-a folosit pentru lucrul cu fisiere binare

-- numpy -> s-a folosit pentru lucrul cat mai eficient cu tablouri n-dimensionale (vectori,matrice,etc.) --

-- pyautogui -> s-a folosit pentru programarea functionalitatii programului ce permite chatbot-ului sa realizeze screenshot-uri/print-screen-uri --


# Mod de functionare program:
Am creat baza de date a programului sub forma unui fisier de tip .json. In acest fisier s-au introdus posibile intrebari,raspunsuri,iar fiecareia din acestea doua li s-a atribuit si cate un topic special,astfel incat ,in cazul in care intrebarea apartine unui anume topic,chatbot-ul sa poata raspunde,cu ajutorul predictiilor generate de inteligenta arificiala tot cu un raspuns din acelasi topic. In situatia in care utilizatorul ii spune bot-ului ca trebuie sa plece sau raspunde cu nu,in situatia in care acesta il intreaba daca il mai poate ajuta si cu altceva,conditia de oprire a programului va fi satisfacuta,si ,astfel,programul se va opri intr-un mod automat.

Dezavantajul acestui program este acela ca baza de date va trebui reactualizata manual de fiecare data cand utilizatorul doreste ca chatbot-ul sa ii ofere si alte raspunsuri,sau sa faca si alte sarcini,fata de cele de deja au fost implementate.Acest lucru nu a fost introdus ca un feature al programului,deoarece,la fiecare update al fisierului .json,fisierul training.py va trebui rulat din nou,astfel incat inteligenta artificiala sa poata genera un raspuns aleatoriu al bot-ului,la intrebarea adresata de catre urilizator.

Pentru a face cu atat mai complex programul,am folosit un wordnetlemmatizer pentru a separa propozitiile in cuvinte si pentru a elimina duplicatele.In acest fel,in momentul in care utilizatorul pune o intrebare bot-ului ,aceasta va fi si ea la randul ei separata in cuvinte,iar pe baza NLP,programul va stabili prin intermediul unor probabilitati carui topic/in ce topic poate fi incadrata intrebarea ,prin compararea cuvintelor din propozitia citita de la tastatura cu a acelora din fisierul de tip json.Pentru a eficientiza acest proces,am facut astfel incat programul sa ignore semenele de punctuatie,respectiv literele mari si sa trateze toate cuvintele articulate ca un cuvant simplu (spre exemplu:munca,muncii,munci-vor fi tratate de catre program ca niste cuvinte asemanatoare ca inteles).

Pentru a rula programul (care activeaza chatbot-ul),dupa rularea programului training.py,ce antreneaza modelul AI,se va rula programul chatbot.py




