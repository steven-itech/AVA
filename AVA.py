#Importation des bibliothèques.
import ctypes
import pyttsx3
import os
import datetime
import speech_recognition as sr
import subprocess
import wget
import wikipedia
import webbrowser
import smtplib
import screen_brightness_control as sbc
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import messagebox

ctypes.windll.kernel32.SetConsoleTitleW("AVA :")

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

#Fonction permettant d'interpréter un texte en parole. (text-to-speech)
def tts(message):
    
    engine.say(message)
    engine.runAndWait()
    
#Fonction permettant de nettoyer la console.
def clean():
    
    os.system("cls")
    
clean()

if ctypes.windll.shell32.IsUserAnAdmin():
    
    pass

elif not ctypes.windll.shell32.IsUserAnAdmin():
    
    tts("Veuillez exécuter AVA via l'invite de commande en mode administrateur afin de l'utiliser de manière optimale !")
    messagebox.showinfo(title="AVA :", message="Veuillez exécuter AVA via l'invite de commande en mode administrateur afin de l'utiliser de manière optimale !")
    
    os.system("pause > nul")
    
    quit()
    
#Fonction permettant de saluer l'utilisateur, en fonction de l'heure qu'il est.
def current_hour():
    
    #Variable permettant de récupérer l'heure qu'il est.
    current_hour = int(datetime.datetime.now().hour)

    if 0 <= current_hour < 12:
       
        greeting = "Bonjour, je suis AVA votre assistante virtuelle à reconnaissance vocale et vous souhaite une excellente matinée !"
        
    elif 12 <= current_hour < 18:
        
        greeting = "Bonjour, je suis AVA, votre assistante virtuelle à reconnaissance vocale et vous souhaite un bon après-midi !"
    
    elif current_hour >= 18 and current_hour != 0:
        
        greeting = "Bonsoir, je suis AVA votre assistante virtuelle à reconnaissance vocale et vous souhaite une excellente soirée !" 
        
    #Instruction permettant de transmettre le résultat de la variable greeting.
    return greeting + "Que puis-je faire pour vous ?"
        
greeting = current_hour()
tts(greeting)
        
#Fonction permettant d'ouvrir un logiciel ou une application.
def open(application):
   
    subprocess.run([application])

#Fonction permettant d'accéder à une ressource sur le web.
def web(search_engine):
   
    webbrowser.open(search_engine)
    
#Fonction permettant l'envoi d'un courriel.
def mail():
    
    clean()
    
    tts("Quelle est votre adresse électronique ?")
    email = input("Quelle est votre adresse électronique ? : ")
    
    clean()
    
    tts("Quel est votre mot de passe d'application ?")
    password = input("Quel est votre mot de passe d'application ? : ")
    
    clean()
    
    tts("Quelle est l'adresse électronique de votre destinataire ?")
    recipient = input("Quelle est l'adresse électroniqque de votre destinataire ? : ")
    
    clean()
    
    tts("Quel est le sujet de votre courriel ?")
    subject = input("Quel est le sujet de votre courriel ? : ")
    
    clean()
    
    tts("Quel est le message de votre courriel ?")
    
    content = []
    
    tts("Veuillez saisir le message de votre courriel, puis laisser une ligne vide afin de marquer la fin de celui-ci !")
    messagebox.showwarning(title="AVA : ", message="Veuillez saisir le message de votre courriel, puis laisser une ligne vide afin de marquer celui-ci !")
    
    while True:
        
        message = input()
        
        clean()
        
        if message:
            
            content.append(message + "\n\n")
            
        else:
            
            try:
            
                msg = MIMEMultipart()
                
                msg["From"] = email
                msg["To"] = recipient
                msg["Subject"] = subject
                msg.attach(MIMEText("".join(content), "plain"))  
                
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(email, password)
                server.sendmail(email, recipient, msg.as_string())  
                server.quit()
                
                break
            
            except smtplib.SMTPException as e:
                
                if isinstance(e, smtplib.SMTPAuthenticationError):
                    
                    tts("Votre courriel n'a pas pu être envoyé, car vos identifiants sont invalides !")
                    messagebox.showerror(title="AVA : ", message="Votre courriel n'a pas pu être envoyé, car vos indentifiants sont invalides !")
                    
                    mail()
                    
                elif isinstance(e, smtplib.SMTPServerDisconnected):
                    
                    tts("Votre courriel n'a pas pu être envoyé, car le serveur SMTP s'est déconnecté de manière innatendue !")
                    messagebox.showerror(title="AVA : ", message="Votre courriel n'a pas pu être envoyé, car le serveur SMTP s'est déconnecté de manière innatendue !")
                    
                    mail()
                    
                elif isinstance(e, smtplib.SMTPResponseException):
                    
                    tts("Votre courriel n'a pas pu être envoyé, car le serveur SMTP a renvoyé un code erreur !")
                    messagebox.showerror(title="AVA : ", message="Votre courriel n'a pas pu être envoyé, car le serveur SMTP a renvoyé un code erreur !")
                    
                    mail()
                 
                elif isinstance(e, smtplib.SMTPSenderRefused):
                    
                    tts("Votre courriel n'a pas pu être envoyé, car votre adresse électronique est invalide !")
                    messagebox.showerror(title="AVA : ", message="Votre courriel n'a pas pu être envoyé, car votre adresse électronique est invalide !")
                    
                    mail()   
                
                elif isinstance(e, smtplib.SMTPRecipientsRefused):
                    
                    tts("Votre courriel n'a pas pu être envoyé, car l'adresse électronique de votre destinataire est invalide !")
                    messagebox.showerror(title="AVA : ", message="Votre courriel n'a pas pu être envoyé, car l'adresse eléctronique de votre destinataire est invalide !")
                    
                    mail()
                    
                elif isinstance(e, smtplib.SMTPDataError):
                    
                    tts("Votre courriel n'a pa pu être envoyé, car le serveur SMTP a refusé d'accepter les données de votre message !")
                    messagebox.showerror(title="AVA : ", message="Votre courriel n'a pas pu être envoyé, car le serveur SMTP a refusé d'accepter les données de votre message !")
                    
                    mail()
                    
                elif isinstance(e, smtplib.SMTPConnectError):
                    
                    tts("Votre courriel n'a pas pu être envoyé, car une erreur s'est produite lors de l'établissement de la connexion au serveur SMTP !")
                    messagebox.showerror(title="AVA : ", message="Votre courriel n'a pas pu être envoyé, car une erreur s'est produite lors de l'établissement de la connexion au serveur SMTP !")
                    
                    mail()
                    
                elif isinstance(e, smtplib.SMTPHeloError):
                    
                    tts("Votre courriel n'a pas pu être envoyé, car le serveur SMTP a refusé le message : HELO !")
                    messagebox.showerror("Votre courriel n'a pas pu être envoyé, car le serveur SMTP a refusé le message : HELO !")
                    
                    mail()
                    
                elif isinstance(e, smtplib.SMTPNotSupportedError):
                    
                    tts("Votre courriel n'a pas pu être envoyé, car la commande ou l'option tentée n'est pas prise en charge par le serveur SMTP !")
                    messagebox.showerror("Votre courriel n'a pas pu être envoyé, car la commande ou l'option tentée n'est pas prise en charge par le serveur SMTP !") 
                    
                    mail()
                    
                else:
                    
                    tts("Votre courriel a été envoyé avec succès au destinataire !")
                    messagebox.showerror(title="AVA : ", message="Votre courriel a été envoyé avec succès au destinataire !")
                    
                    ava()
                    
#Dictionnaire permettant d'ouvrir le navigateur Chrome.
browser = {

    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe"
}

#Dictionnaire répertoriant les différents moteurs de recherche utilisés par autrui.
search_engines = {
    
    "google": "https://google.com",
    "google avancé": "https://www.google.com/advanced_search",
    "bing": "https://bing.com",
    "yahoo": "https://yahoo.com",
    "yandex": "https://yandex.com",
    "brave": "https://search.brave.com/",
    "duckduckgo": "https://duckduckgo.com",
    "qwant": "https://www.qwant.com/",
    "ecosia": "https://www.ecosia.org/",
}
         
electronic_messaging = {
    
    "gmail": "https://mail.google.com",
    "yahoo": "https://fr.mail.yahoo.com",
    "outlook": "https://outlook.live.com/mail/0/",
    "proton": "https://mail.proton.me/u/0/inbox/"
}

#Dictionnaire permettant d'ouvrir le logiciel Adobe Acrobat Reader.
adobe = {
    
    "acrobat": r"C:\Program Files\Adobe\Acrobat DC\Acrobat\Acrobat.exe"
}

#Fonction permettant d'écouter l'entrée audio du microphone, afin d'effectuer les différentes opérations du programme.
def microphone():
    
    listener = sr.Recognizer()
    
    with sr.Microphone() as source:
        
        try:
            
            listener.pause_threshold = 3
            voice = listener.listen(source)
            
            keyword = listener.recognize_google(voice, language="fr-Fr")
            keyword = keyword.lower()
            
            return keyword
        
        except sr.exceptions.UnknownValueError:
            
            tts("Je n'ai pas compris votre demande, veuillez vous rapprocher de votre microhpone ou articuler lorsque vous parler !") 
            messagebox.showinfo(title="AVA :", message="Je n'ai pas compris votre demande, veuillez vous rapprocher de votre microhpone ou articuler lorsque vous parler !")
            
            ava()
        
#Fonction principale du programme.
def ava():
    
        try:
    
            clean()
        
            keyword = microphone()
            
            if "antivirus" in keyword:
                
                subprocess.Popen(["cmd", "/k", "python", os.path.join(os.path.dirname(os.path.abspath(__file__)), "antivirus.py")], shell=True)
                ava()
                
            elif "mise à jour système" in keyword:
                
                update = subprocess.Popen(["powershell.exe", "Get-WindowsUpdate"], shell=True, stdout=subprocess.PIPE)
                stdout, _ = update.communicate()
                
                if b"Status" in stdout:
                    
                    informations_1 = "Les mises à jour système présentes sur votre ordinateur sont en cours d'installation !"
                    informations_2 = "Veuillez patienter, cette opération peut prendre plusieurs minutes !"
                    
                    tts(informations_1 + informations_2)
                    install = subprocess.Popen(["powershell.exe", "Install-WindowsUpdate -AcceptAll"], shell=True)
                    
                    if install.wait() == 0:
                        
                        tts("Les mises à jour viennent d'être installées !")
                        messagebox.showinfo(title="AVA :", message="Les mises à jour viennent d'être installées !")
                        
                    elif install.wait() == 1:
                        
                        tts("Les mises à jour n'ont pas pu être installées !")
                        messagebox.showinfo(tile="AVA :", message="Les mises à jour n'ont pas pu être installées !")
                        
                    else:
                        
                        informations_1 = "Aucune mise à jour n'est disponible pour le moment !\n"
                        informations_2 = "Effectuez une analyse une prochaine fois afin de savoir si cela est encore le cas !"
                        
                        tts(informations_1 + informations_2)
                        messagebox.showinfo(title="AVA :", message=informations_1 + informations_2)
                    
                else:
                    
                    while True:
                    
                        tts("Afin d'effectuer les mises à jour système présentes sur votre ordinateur, veuillez installer le module PS-WindowsUpdate !")
                        messagebox.showinfo(title="AVA :", message="Afin d'effectuer les mises à jour logicielles présentes sur votre ordinateur, veuillez installer le module PS-WindowsUpdate !")
                        
                        tts("Souhaitez-vous installer le module PS-WindowsUpdate, afin d'effectuer les mises à jour système présentes sur votre ordinateur ? :")
                        choice = input("Souhaitez-vous installer le module PS-WindowsUpdate, afin d'effectuer les mises à jours logicielles présentes sur votre ordinateur ? : ")
                        
                        clean()
                        
                        if "oui" in choice.lower():
                            
                            install = subprocess.Popen(["powershell.exe", "Install-Module -Name PSWindowsUpdate -Force"], shell=True) 
                            
                            if install.wait() == 0:
                                
                                tts("Le module PS-WindowsUpdate vient d'être installé !")
                                messagebox.showinfo(title="AVA :", message="Le module PS-WindowsUpdate vient d'être installé !")
                                
                                break
                                
                            elif install.wait() == 1:
                                
                                tts("Le module PS-WindowsUpdate n'a pas pu être installé !")    
                                messagebox.showinfo(title="AVA :", message="Le moddule PS-WindowsUpdate n'a pas pu être installé !")   
                                
                                break
                                
                            else: 
                                
                                tts("Veuillez choisir entre oui ou non !")   
                                messagebox.showerror(title="AVA :", message="Veuillez choisir entre oui ou non !")     
                                
                                break
                        
                        elif "non" in choice.lower():
                            
                            break
                        
            elif "mise à jour applicative" in keyword:
                
                update = subprocess.Popen(["winget", "update"], stdout=subprocess.PIPE)
                stdout, _ = update.communicate()
                
                if b"Nom" in stdout:
                    
                    informations_1 = "Des mises à jour applicatives sont présentes sur votre ordinateur !"
                    informations_2 = "Si elles ne sont pas explicites, elles seront installées automatiquement, tandis que les autres devront être effectuées manuellement !"
                    informations_3 = "Veuillez patienter, cette opération peut prendre plusieurs minutes !"
                    
                    tts(informations_1 + informations_2 + informations_3)
                    
                    install = subprocess.Popen(["winget", "update", "--all", "--include-unknown"], stdout=subprocess.PIPE) and subprocess.Popen(["winget", "update", "--all", "--include-unknown"], shell=True)
                    
                    if install.wait() == 0:
                        
                        tts("Les mises à jour non explicites viennent d'être installées !")
                        messagebox.showinfo(title="AVA :", message="Les mises à jour non explicites viennent d'être installées !")
                    
                    if b"Les packages suivants" in stdout:  
                        
                        tts("Pour mettre à jour les logiciels nécessitant un ciblage explicite, veuillez désinstaller le logiciel en question et télécharger sa nouvelle version !")
                        messagebox.showinfo(title="AVA :", message="Pour mettre à jour les logiciels nécessitant un ciblage explicite, veuillez désinstaller le logiciel en question et télécharger sa nouvelle version !")  
                            
                else:
                    
                    while True:
                    
                        tts("Afin d'effectuer les mises à jour applicatives présentes sur votre ordinateur, veuillez installer le gestionnaire de paquets de Microsoft !")
                        messagebox.showinfo(title="AVA :", message="Afin d'effectuer les mises à jour logicielles présentes sur votre ordinateur, veuillez installer le gestionnaire de paquets de Microsoft !")
                        
                        tts("Souhaitez-vous installer le gestionnaire de paquets de Microsoft, afin d'effectuer les mises à jours applicatives présentes sur votre ordinateur ? :")
                        choice = input("Souhaitez-vous installer le gestionnaire de paquets de Microsoft, afin d'effectuer les mises à jours applicatives présentes sur votre ordinateur ? : ")
                        
                        clean()
                        
                        if "oui" in choice.lower():
                            
                            wget.download("https://github.com/microsoft/winget-cli/releases/download/v1.7.10861/Microsoft.DesktopAppInstaller_8wekyb3d8bbwe.msixbundle", os.path.join(os.path.dirname(os.path.abspath(__file__)), "winget.msixbundle"))
                            subprocess.run(install)
                        
                        elif "non" in choice.lower():
                            
                            ava()
                            
                        else:
                            
                            tts("Veuillez choisir entre oui ou non !")   
                            messagebox.showerror(title="AVA :", message="Veuillez choisir entre oui ou non !")     
                                    
                            break

            elif keyword in browser:
                
                clean()
                
                tts(f"Ouverture du navigateur : {keyword}")
                open(browser[keyword])
                
            elif keyword in search_engines:
                
                clean()
                
                tts(f"Accès au moteur de recherche : {keyword}")
                web(search_engines[keyword])
        
            elif keyword in electronic_messaging:
                
                clean()
            
                tts(f"Accès à la messagerie électronique : {keyword}")
                web(electronic_messaging[keyword])
            
            elif keyword in adobe:
                
                clean()
                
                tts(f"Ouverture du logiciel : {keyword} Acrobat.")
                open(adobe[keyword])
            
            elif "courriel" in keyword:

                mail()
                        
            elif "youtube" in keyword:
                
                subprocess.Popen(["cmd", "/k", "python", os.path.join(os.path.dirname(os.path.abspath(__file__)), "youtube.py")], shell=True)
                ava()

            elif "recherche" in keyword:
                
                clean()
                
                tts("Quel sujet souhaitez-vous rechercher ?")
                subject = input("Quel sujet souhaitez-vous rechercher ? : ")
                
                clean()

                wikipedia.set_lang("fr")
                
                informations = wikipedia.summary(subject)
                
                print(informations)
                tts(informations)
                
                os.system("pause > nul")
                clean()
                
                tts("Souhaitez-vous obtenir un document PDF du sujet ?")
                pdf = input("Souhaitez-vous obtenir un document PDF du sujet ? : ")
                
                clean()
                
                if "oui" in pdf:
                
                    subprocess.Popen(["cmd", "/k", "python", os.path.join(os.path.dirname(os.path.abspath(__file__)), "wiki.py")], shell=True)
                    ava()
                
                elif "non" in pdf:
                    
                    ava()
                    
            elif "météo" in keyword:
                
                clean()
                
                subprocess.Popen(["cmd", "/k", "python", os.path.join(os.path.dirname(os.path.abspath(__file__)), "meteo.py")], shell=True)
                ava()
                        
            elif "radio" in keyword:
                
                clean()
                
                subprocess.Popen(["cmd", "/k", "python", os.path.join(os.path.dirname(os.path.abspath(__file__)), "radio.py")], creationflags=subprocess.CREATE_NEW_CONSOLE)
                ava()
                    
            elif "transfert" in keyword:
                
                clean()
                
                tts("Veuilez copier le fichier client.py sur une autre machine, afin de pouvoir effectuer le transfert !")
                print("Veuillez copier le fichier client.py sur une autre machine, afin de pouvoir effectuer le transfert !")

                messagebox.showwarning(title="AVA :", message="Veuillez copier le fichier client.py sur une autre machine, afin de poivoir effectuer le transfert !")
                subprocess.Popen(["cmd", "/k", "python", os.path.join(os.path.dirname(os.path.abspath(__file__)), "server.py")], creationflags=subprocess.CREATE_NEW_CONSOLE)

                ava()
                
            elif "pdf" in keyword:
                
                subprocess.Popen(["cmd", "/k", "python", os.path.join(os.path.dirname(os.path.abspath(__file__)), "pdf.py")], shell=True)
                ava()
            
            elif "luminosité" in keyword:
                
                clean()
                
                tts("Quel pourcentage de luminosité souhaitez-vous pour votre écran d'ordinateur ?")
                percentage = int(input("Quel pourcentage de luminosité souhaitez-vous pour votre écran d'ordinateur ? : "))
                
                clean()
                
                sbc.set_brightness(percentage)
                
        except KeyboardInterrupt:
            
            tts("Souhaitez-vous quitter AVA ?")
            choice = input("Souhaitez-vous quitter AVA ? : ")
            
            clean()
            
            if "oui" in choice.lower():
                
                tts("Au revoir !")
                messagebox.showinfo(title="AVA :", message="Au revoir !")
                
                quit()
                
            elif "non" in choice.lower():
                
                ava()
                
            else:
                
                tts("Veuillez choisir une option valide, par oui ou non !")
                messagebox.showerror(title="AVA :", message="Veuillez choisir une option valide, par oui ou non !")
            
if __name__ == "__main__":
    
    while True:
       
        ava()