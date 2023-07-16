import speech_recognition as sr
import pyttsx3 as ttx
import pywhatkit 
import datetime

listener = sr.Recognizer()
engine = ttx.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', 'french')

def parle(text):
    engine.say(text)
    engine.runAndWait()
    
def ecoute():
    try:
        with sr.Microphone() as source:
            print("Parler ")
            voix = listener.listen(source)
            command = listener.recognize_google(voix, language='fr-FR')
    except:
        pass
    return command

def assistante():
    command = ecoute()
    print(command)
    if 'bonjour' in command:
        parle('bonjour comment vous allez ?')
    elif 'Je vais bien et toi?' in command:
        parle('Oui je vais que puis-je pour vous ?')
    elif 'joue la chanson de ' in command:
        chanteur = command.replace('joue la chanson de ','')
        print(chanteur)
        pywhatkit.playonyt(chanteur)
    elif 'heure' in command:
        heure = datetime.datetime.now().strftime("%H:%M")
        parle('il est'+heure)
    elif 'ton nom' in command:
        parle('Mon nom est Darell pour vous embêter')
        
while True:
    assistante()