import ctypes
import pyttsx3
import os
import requests
from tkinter import messagebox

#Afficher comme titre "Wikipedia :"
ctypes.windll.kernel32.SetConsoleTitleW("Wikipedia :")

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

#Fonction permettant de traduire un texte en parole. (text-to-speech)
def tts(message):
    
    engine.say(message)
    engine.runAndWait()

#Fonction permettant de nettoyer la console.
def clean():
    
    os.system("cls")
    
def wikipedia():
    
    while True:
    
        clean()

        tts("Quel sujet souhaitez-vous rechercher ?")
        subject = input("Quel sujet souhaitez-vous rechercher ? : ")
        
        clean()

        if subject.isalpha():
            
            pass
            
        elif not subject.isalpha():
            
           tts("Veuillez transmettre le nom de votre sujet via des lettres !")
           messagebox.showerror(title="Wikipedia :", message="Veuillez transmettre le nom de votre sujet via des lettres !")
        
        tts("Dans quelle langue souhaitez-vous obtenir les informations concernant le sujet ? : (français ou anglais)")
        lang = input("Dans quelle langue souhaitez-vous obtenir les informations concernant le sujet ? : (français ou anglais) ")
        
        clean()
        
        if lang.isalpha():
            
            pass
        
        elif not lang.isalpha():
            
            tts("Veuillez choisir une langue via des lettres !")
            messagebox.showerror(title="Wikipedia :", message="Veuillez choisir une langue via des lettres !")
            
            wikipedia()
            
        else: 
            
            tts("Cette langue n'est pas disponible, veuillez choisir entre le français et l'anglais !")
            messagebox.showerror()
        
            wikipedia()
            
        if "français" in lang:
            
            url = "https://fr.wikipedia.org/"
            api = "api/rest_v1/page/pdf/"

            address = url + api + subject
            name = subject + ".pdf"

            r = requests.get(address, stream=True)

            with open(name, "wb") as pdf:
            
                for chunk in r.iter_content(chunk_size=4096):
                    
                    if chunk:
                        
                        pdf.write(chunk)
                        
        elif "anglais" in lang:
            
            url = "https://en.wikipedia.org/"
            api = "api/rest_v1/page/pdf/"

            address = url + api + subject
            name = subject + ".pdf"

            r = requests.get(address, stream=True)

            with open(name, "wb") as pdf:
            
                for chunk in r.iter_content(chunk_size=4096):
                    
                    if chunk:
                        
                        pdf.write(chunk)      
                        
        tts("Souhaitez-vous continuer à obtenir des documents PDF ?")
        choice = input("Souhaitez-vous continuer à obtenir des documents PDF ? : ")
                            
        clean()
                            
        if "oui" in choice:
            
            continue
                            
        elif "non" in choice:
           
            quit()
            
        else:
            
            tts("Veuillez choisir une option valide, par oui ou non !")
            messagebox.showerror(title="Wikipedia :", message="Veuillez choisir une option valide, par oui ou non !")
            
            wikipedia()