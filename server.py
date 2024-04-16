import ctypes
import pyttsx3
import ipaddress
import os
import socket
from tkinter import messagebox

# Afficher comme titre "Serveur de fichiers :"
ctypes.windll.kernel32.SetConsoleTitleW("Serveur de fichiers :")

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

# Fonction permettant de traduire en texte en parole. (text-to-speech)
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
    
    tts("Quel est le port d'ecoute du serveur de fichiers ?")
    port_input = input("Quel est le port d'écoute du serveur de fichiers ? : ")

    clean()

    if not port_input.isdigit():
        
        tts("Veuillez transmettre un port valide, compris entre 0 et 65535 !")
        messagebox.showerror(title="Client :", message="Veuillez transmettre un port valide, compris entre 0 et 65535 !")
    
    else:
        
        port = int(port_input)
        break

server.bind((ip, port))
server.listen(60)

tts(f"Le serveur de fichiers est en cours d'écoute sur le port : {port}")
print(f"Le serveur de fichiers est en cours d'écoute sur le port : {port}")

while True:
    
    conn, addr = server.accept()
    
    tts(f"Une adresse IP : {addr} est connecté au serveur de fichiers !")
    print(f"Une adresse IP : {addr} est connecté au serveur de fichiers !")

    tts("Veuillez transmettre le chemin d'accès du fichier que vous souhaitez transférer à l'hôte distant !")
    file_path = input("Veuillez transmettre le chemin d'accès du fichier que vous souhaitez transférer à l'hôte distant : ")

    clean()

    with open(file_path, "rb") as file:
        
        while True:
            
            data = file.read(1024)
            
            if not data:
                
                break
           
            conn.send(data)

    tts("Le fichier a été envoyé à l'hôte distant !")
    print("Le fichier a été envoyé à l'hôte distant !")

    conn.close()

    os.system("pause > nul")
    
    quit()