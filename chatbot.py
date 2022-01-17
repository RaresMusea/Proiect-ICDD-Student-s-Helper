# Programul responsabil de functionalitatea Chatbot-ului
import random
import json
import pickle
from nltk import probability
from nltk.tokenize import word_tokenize
from nltk.tokenize.regexp import WhitespaceTokenizer
import numpy as np
import nltk
import webbrowser
import pyautogui

from nltk.stem import WordNetLemmatizer

# Utilizam biblioteci precum tensorflow si keras,ce au fost utilizate si in crearea modelului AI ,ce utilizeaza NLP,pentru a putea incarca si in programul principal aceste elemente()
from tensorflow.keras.models import load_model

lematizator = WordNetLemmatizer()
dataset = json.loads(open('intents.json').read())

cuvinte = pickle.load(open('cuvinte.pkl', 'rb'))
clase = pickle.load(open('clase.pkl', 'rb'))

model = load_model('chatbot_AI.model')

# Functii:
# Functie pentru spargerea propozitiei in mai multe cuvinte si eliminarea duplicatelor.In acest fel,input-ul de la tastatura va avea o forma foarte asemanatoare cu outputul generat de programul training.py


def propozitie(prop):
    cuvinte_prop = nltk.word_tokenize(prop)
    cuvinte_prop = [lematizator.lemmatize(word) for word in cuvinte_prop]
    return cuvinte_prop

# Functie pentru prelucrarea container-ului utilizat in programul chatbot.py
# Aceasta functie va transforma o propozitie intr-un container de cuvinte


def prelucrare_container(prop):
    prop_cuvinte = propozitie(prop)
    cont = [0]*len(cuvinte)
    for cuv in prop_cuvinte:
        for i, cuvant in enumerate(cuvinte):
            if cuvant == cuv:
                cont[i] = 1
    return np.array(cont)


# Functie pentru alegerea tag-ului/a topic-ului specific intrebarii/replicii,dar si a raspunsului pe care chatbot-ul il va returna

def guess_topic(propozitie):
    sir_cuvinte = prelucrare_container(propozitie)
    resolve = model.predict(np.array([sir_cuvinte]))[0]
    ERROR_TRESHHOLD = 0.25
    results = [[i, r] for i, r in enumerate(resolve) if r > ERROR_TRESHHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': clase[r[0]], 'probability': str(r[1])})
    return return_list

# Functie responsabila de afisarea raspunsurilor chatbot-ului


def obtine_raspuns(intentii, intentii_json):
    topic = intentii[0]['intent']
    lista_intentii = intentii_json['intents']
    for i in lista_intentii:
        if i['tag'] == topic:
            rezultat = random.choice(i['responses'])
            break
    return rezultat


# Aceasta functie a fost folosita in mod special pentru automatizarea sarcinilor la care chatbot-ul va fi supus de catre utilizator

def topic_special(topic):
    tag = topic[0]['intent']

    if tag == 'caminul 1':
        url = 'https://campus.ulbsibiu.ro/ro/spatii-de-cazare/caminul-1/'
        chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
        webbrowser.register(
            'chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab(url)

    if tag == 'caminul 2':
        url = 'https://campus.ulbsibiu.ro/ro/spatii-de-cazare/caminul-2/'
        chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
        webbrowser.register(
            'chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab(url)

    if tag == 'caminul 3':
        url = 'https://campus.ulbsibiu.ro/ro/spatii-de-cazare/caminul-3/'
        chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
        webbrowser.register(
            'chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab(url)

    if tag == 'caminul 4':
        url = 'https://campus.ulbsibiu.ro/ro/spatii-de-cazare/caminul-4/'
        chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
        webbrowser.register(
            'chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab(url)

    if tag == 'caminul 6':
        url = 'https://campus.ulbsibiu.ro/ro/spatii-de-cazare/caminul-6/'
        chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
        webbrowser.register(
            'chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab(url)

    if tag == 'caminul 7':
        url = 'https://campus.ulbsibiu.ro/ro/spatii-de-cazare/caminul-7/'
        chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
        webbrowser.register(
            'chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab(url)

    if tag == 'web':
        url = ''
        chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
        webbrowser.register(
            'chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab(url)
    elif tag == 'internet':
        core = input("")
        a = 'https://'
        url = a+core
        chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
        webbrowser.register(
            'chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab(url)
    elif tag == "screenshot":
        printscreen = pyautogui.screenshot()
        printscreen.save(
            r'D:\Programming\machine learning\printscreens\poza.png')
    elif tag == 'music':
        app = input(
            "Ce platforma de streaming doresti sa folosesti? Alege dintre Spotify,Youtube sau Soundcloud!")
        if app == 'Spotify' or app == 'spotify':
            url = 'https://www.spotify.com/us/'
            chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
            webbrowser.register(
                'chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)
        elif app == 'Soundcloud' or app == 'soundcloud':
            url = 'https://soundcloud.com/'
            chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
            webbrowser.register(
                'chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)
        elif app == 'youtube' or app == 'Youtube':
            url = 'https://www.youtube.com/'
            chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
            webbrowser.register(
                'chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)


print("PROGRAM:Salut!Fa cunostina cu Thomas!")

# Runtime program principal
run = True
while run == True:
    mesaj = input("")
    top = guess_topic(mesaj)
    res = obtine_raspuns(top, dataset)
    print(res)
    topic_special(top)
    tag = top[0]['intent']
    if tag == 'goodbye':
        run = False
