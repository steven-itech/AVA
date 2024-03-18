import ctypes
import pyttsx3
import os
import socket

ctypes.windll.kernel32.SetConsoleTitleW("Serveur de fichiers :")

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def tts(message):
    
    engine.say(message)
    engine.runAndWait()

def clean():
    
    os.system("cls")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tts("Quelle est l'adresse IP du serveur de fichiers ? ")
ip = input("Quelle est l'adresse IP du serveur de fichiers ? : ")

clean()

tts("Quel est le port d'ecoute du serveur de fichiers ?")
port = int(input("Quel le port d'écoute du serveur de fichiers ? : "))

clean()

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
