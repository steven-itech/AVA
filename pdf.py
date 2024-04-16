import ctypes
import pyttsx3
import os
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from PyPDF2 import PdfReader
from deep_translator import GoogleTranslator
from gtts import gTTS

ctypes.windll.kernel32.SetConsoleTitleW("Traducteur PDF :")

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def tts(message):
    
    engine.say(message)
    engine.runAndWait()

def clean():
    
    os.system("cls")

while True:
    
    tts("Dans quelle langue souhaitez-vous traduire le document PDF ?")
    lang = input("Dans quelle langue souhaitez-vous traduire le document PDF ? : ")

    clean()
    
    if lang.isalpha():
        
        pass
    
    elif not lang.isalpha():
        
        tts("Veuillez choisir le nom d'une langue via des lettres !")
        messagebox.showerror(title="Traducteur PDF :", message="Veuillez chioisir le nom d'une langue viad des lettres !")

    explorer = askopenfilename()

    with open(explorer, "rb") as file:
        
        pdf = PdfReader(file)
        text = ""
        
        for page in range(len(pdf.pages)):
            
            text += pdf.pages[page].extract_text()

        translated = GoogleTranslator(source="auto", target=lang).translate(text)
        
        speech = gTTS(text=translated, lang=lang, slow=False)
        speech.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "translated.mp3"))
        
        tts("Votre document PDF a été traduit avec succès !")
        messagebox.showinfo(title="Traducteur PDF :", message="Votre document PDF a été traduit avec succès !")

        tts("Souhaitez-vous traduire un autre document PDF ?")
        choice = input("Souhaitez-vous traduire un autre document PDF ? : ")

        clean()

        if "oui" in choice.lower():
            
            continue
       
        elif "non" in choice.lower():
           
            break
        
        else:
            
            tts("Veuillez choisir une option valide, par oui ou par non !")
            messagebox.showerror(title="Traducteur PDF :", message="Veuillez choisir une option valide, pas oui par non !")