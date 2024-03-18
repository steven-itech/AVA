import ctypes
import pyttsx3
import os
import datetime
import speech_recognition as sr
import subprocess
import webbrowser
import smtplib
import socket
import tqdm
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from tkinter import messagebox
from newspaper import Source
import screen_brightness_control as sbc

ctypes.windll.kernel32.SetConsoleTitleW("AVA")

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def tts(message):
    
    engine.say(message)
    engine.runAndWait()

def clean():
    
    os.system("cls")

def current_hour():
    
    current_hour = int(datetime.datetime.now().hour)
    
    if 0 <= current_hour < 12:
       
        presentation = "Je suis AVA, votre assistante virtuelle à reconnaissance vocale et vous souhaite une excellente matinée !"
        message = "Que puis-je faire pour vous ?"
    
    elif 12 <= current_hour < 18:
        
        presentation = "Je suis AVA, votre assistante virtuelle à reconnaissance vocale et vous souhaite un bon après-midi !"
        message = "Que puis-je faire pour vous ?"
    
    elif current_hour >= 18 and current_hour != 0:
        
        presentation = "Je suis AVA, votre assistante virtuelle à reconnaissance vocale et vous souhaite une excellente soirée !"
        message = "Que puis-je faire pour vous ?"
    
    tts(presentation + message)

current_hour()

def open(application):
   
    subprocess.Popen([application])

def web(search_engine):
   
    webbrowser.open(search_engine)
    
def mail(smtp_server, smtp_port, email, password, recipient, subject, message, attachments=[]):
    
    clean()
    
    email_message = MIMEMultipart()
    
    email_message["From"] = email
    email_message["To"] = ", ".join(recipient)
    email_message["Subject"] = subject
    
    email_message.attach(MIMEText(message, "plain"))
    
    for attachment in attachments:
        
        filename = os.path.basename(attachment)
        attachment_part = MIMEBase("application", "octet-stream")
        
        with open(attachment, "rb") as file:
            
            attachment_part.set_payload(file.read())
       
        encoders.encode_base64(attachment_part)
        
        attachment_part.add_header("Content-Disposition", f"attachment; filename={filename}")
        email_message.attach(attachment_part)
    
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        
        server.starttls()
        server.login(email, password)
        server.sendmail(email, recipient, email_message.as_string())
 
def microphone():
    
    listener = sr.Recognizer()
    
    with sr.Microphone() as source:
        
        listener.pause_threshold = 5
        voice = listener.listen(source)
        
        command = listener.recognize_google(voice, language="fr-Fr")
        command = command.lower()
    
    return command

electronic_messaging = {
    
    "Messagerie électronique : \n\n"
    "gmail": "https://mail.google.com",
    "yahoo": "https://fr.mail.yahoo.com",
    "outlook": "https://outlook.live.com/mail/0/",
    "proton": "https://mail.proton.me/u/0/inbox \n\n",
}

browser = {
   
    "\nNavigateur : \n\n"
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe"
}

search_engines = {
    
    "\nMoteur de recherche : \n\n"
    "google": "https://google.com",
    "bing": "https://bing.com",
    "yahoo": "https://yahoo.com",
    "duckduckgo": "https://duckduckgo.com",
    "yandex": "https://yandex.com \n\n\n",
}

office_software = {
    
    "\nPDF : \n\n"
    "adobe": r"C:\Program Files\Adobe\Acrobat DC\Acrobat\Acrobat.exe"
}

medias = {
    
    "\nMédias : \n\n"
    "cnews": "https://www.cnews.fr/",
    "dna": "https://www.dna.fr/",
    "parisien": "https://www.leparisien.fr/",
    "figaro": "https://www.lefigaro.fr/",
    "afp": "https://www.afp.com/fr",
}

options = [electronic_messaging, browser, search_engines, office_software, medias]

print("Voici les options disponibles : \n")

for menu in options:
    
    for key in menu.keys():
       
        print(key)

def ava():
    
    command = microphone()
   
    if command in electronic_messaging:
        
        clean()
       
        tts(f"Accès à la messagerie électronique : {command}")
        web(electronic_messaging[command])
    
    elif command in browser:
        
        clean()
        
        tts(f"Ouverture du navigateur : {command}")
        open(browser[command])
    
    elif command in search_engines:
        
        clean()
        
        tts(f"Accès au moteur de recherche : {command}")
        web(search_engines[command])
    
    elif command in office_software:
        
        clean()
        
        tts(f"Ouverture du logiciel : {command} Acrobat.")
        open(office_software[command])
    
    elif "courriel" in command:
        
        clean()
        
        with open("config.txt", "r") as f:
            
            config = [line.strip().split("=")[1] for line in f.readlines()]
        
        smtp_server, smtp_port, sender_email, sender_password, recipient, subject, message, *attachments = config
        
        mail(smtp_server, int(smtp_port), sender_email, sender_password, recipient.split(","), subject, message, attachments)
        tts("Your e-mail has been sent successfully !")
        
        messagebox.showinfo(title="AVA", message="Your e-mail has been sent successfully !")

    elif "transfert" in command:
        
        clean()
        
        subprocess.Popen(["cmd", "/k", "server.py"], creationflags=subprocess.CREATE_NEW_CONSOLE)
        subprocess.Popen(["cmd", "/k", "client.py"], creationflags=subprocess.CREATE_NEW_CONSOLE)
    
    elif command in medias:
        
        clean()
        
        source = Source(medias[command], memoize_articles=False)
        source.build()
        
        tts("Combien d'articles souhaitez-vous lire et écouter ?")
        count = int(input("Combien d'articles souhaitez-vous lire et écouter ? : "))
        
        clean()
        
        read_articles = 0  
        
        for article in source.articles:
            
            if read_articles >= count:  
                
                break
            
            try:
                
                article.download()
                article.parse()
                
                print("Titre de l'article : ", article.title.strip())
                print("Contenu de l'article :\n\n", article.text.strip(), end="\n\n")
                
                info = article.text
                
                tts(info)
                clean()
            
                read_articles += 1
        
            except Exception as e:
                
                print(f"Une erreur est survenue lors de la récupération ou de la lecture de l'article :{e}")
    
    elif "luminosité" in command:
        
        clean()
        
        tts("Quel pourcentage de luminosité souhaitez-vous pour votre écran d'ordinateur ?")
        percentage = int(input("Quel pourcentage de luminosité souhaitez-vous pour votre écran d'ordinateur ? : "))
        
        clean()
        
        sbc.set_brightness(percentage)

if __name__ == "__main__":
    
    while True:
       
        ava()
