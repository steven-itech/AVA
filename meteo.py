import ctypes
import pyttsx3
import os
import requests
from tkinter import messagebox

ctypes.windll.kernel32.SetConsoleTitleW("Météo :")

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def tts(message):
    
    engine.say(message)
    engine.runAndWait()
    
def clean():
    
    os.system("cls")
    
def meteo():

    try:
        
        api_file ="api-openwheatermap.txt"
        
        with open(api_file, "r") as file:
            
            api_key = file.readline().strip()
                
    except FileNotFoundError:
        
        tts("Quelle est votre clé API OpenWheaterMap ?")
                    
        api_key = input("Veuillez transmettre votre clé API OpenWheaterMap : ")
        clean()
                
        if api_key.isalnum():
                
            with open("api-openwheatermap.txt", "w") as file:
                            
                file.write(api_key)
                
        else:
            
            tts("Le format de votre clé API OpenWheaterMap est invalide, celle-ci doit être constituée uniquement de lettres et de chiffres !")
            messagebox.showerror(title="Antivirus :", message="Le format de votre clé API OpenWheaterMap est invalide, celle-ci doit être constituée uniquement de lettres et de chiffres !")

    while True:
        
        tts("Quel est le nom de la ville ?")
        city = input("Quel est le nom de la ville ? : ")
        
        clean()
        
        if city.isalpha():
            
            pass
        
        elif not city.isalpha():
            
            tts("Veuillez écrire le nom de la ville via des lettres !")
            messagebox.showerror(title="Météo :", message="Veuillez écirre le nom de la ville via des lettres !")
        
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=fr"

        response = requests.get(url)

        if response.status_code == 401:
            
            messagebox.showwarning(title="AVA :", message="Votre clé API OpenWheaterMap est invalide, veuillez en transmettre une valide !")
            os.remove(api_file)
            
            meteo()
    
        elif response.status_code == 200:
            
            data = response.json()
            weather = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            
            tts(f"La météo à {city} est : {weather} avec une température de {temperature} °.")
            
            print(f"La météo à {city} est : {weather} avec une température de {temperature} °C.")
            
            os.system("pause > nul")
            clean()
            
            tts("Souhaitez-vous obtenir une prévision météo pour une autre ville ?")
            choice = input("Souhaitez-vous obtenir une prévision météo pour une autre ville ? : ")
            
            clean()
            
            if "oui" in choice:

                continue
            
            if "non" in choice:
                
                break
            
            else:
                
                tts("Veuillez choisir une option valide, par oui ou par non !")
                messagebox.showerror(title="Météo :", message="Veuillez choisir une option valide, par oui ou par non !")   
                       
if __name__ == "__main__":
    
    meteo()