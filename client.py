import ctypes 
import pyttsx3
import ipaddress
import os
import socket
from tkinter import messagebox

# Afficher comme titre "Client :"
ctypes.windll.kernel32.SetConsoleTitleW("Client :")

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

# Fonction permettant de traduire un texte en parole; (text-to-speech)
def tts(message):
    
    engine.say(message)
    engine.runAndWait()

# Fonction permettant de nettoyer la console.
def clean():
    
    os.system("cls")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    
    tts("Quelle est l'adresse IP du serveur de fichiers ?")
    ip = input("Quelle est l'adresse IP du serveur de fichiers ? : ")
    
    clean()

    try: 
        
        ipaddress.ip_address(ip)  
        break
    
    except ValueError:  
        
        tts("Veuillez transmettre une adresse IP valide, composée de chiffres et de points dans sa version 4 ou de chiffres, de lettres et de deux-points dans sa version 6 !")
        messagebox.showerror(title="Client :", message="Veuillez transmettre une adresse IP valide, composée de chiffres et de points dans sa version 4 ou de chiffres, de lettres et de deux-points dans sa version 6 !")

while True:
    
    tts("Quel est le port d'écoute du serveur de fichiers : ")
    port_input = input("Quel est le port d'écoute serveur de fichiers : ")

    clean()

    if not port_input.isdigit():
       
        tts("Veuillez entrer un nombre entier pour le port !")
        messagebox.showerror(title="Client :", message="Veuillez entrer un nombre entier pour le port !")
   
    else:
        
        port = int(port_input)
        break

server.connect((ip, port))

tts("Quel nom souhaitez-vous attribuer au fichier ?")
file_name = input("Quel nom souhaitez-vous attribuer au fichier ? : ")

clean()

with open(file_name, "wb") as file:
    
    while True:
        
        data = server.recv(1024)
        
        if not data:
            
            break
        
        file.write(data)

tts("Le fichier envoyé du serveur de fichiers a été réceptionné !")
print("Le fichier envoyé du serveur de fichiers a été réceptionné !")

server.close()

os.system("pause > nul")

quit()