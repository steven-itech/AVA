import ctypes 
import pyttsx3
import os
import socket

ctypes.windll.kernel32.SetConsoleTitleW("Client :")
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def tts(message):
    
    engine.say(message)
    engine.runAndWait()

def clean():
    
    os.system("cls")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tts("Quelle est l'adresse IP du serveur de fichiers ?")
ip = input("Quelle est l'adresse IP du serveur de fichiers ? : ")

clean()

tts("Quel est le port d'écoute du serveur de fichiers : ")
port = int(input("Quel est le port d'écoute serveur de fichiers : "))

clean()

server.connect((ip, port))

tts("Quel nom souhaitez-vous attribuer au fichier ?")
file_name = input("Quel nom souhaitez vous attribuer au fichier ? : ")

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
