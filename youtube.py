import ctypes
import pyttsx3
import os
import googleapiclient.errors
import webbrowser
from googleapiclient.discovery import build
from tkinter import messagebox

ctypes.windll.kernel32.SetConsoleTitleW("Youtube :")

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def tts(message):
    
    engine.say(message)
    engine.runAndWait()

def clean():
    
    os.system("cls")

def ytb():
    
    try:
        
        api_file = "api-youtube.txt"
        
        with open(api_file, "r") as file:
            
            api_key = file.readline().strip()
   
    except FileNotFoundError:
        
        while True:
            
            tts("Quelle est votre clé API Youtube ?")
            api_key = input("Veuillez transmettre votre clé API Youtube : ")
            
            clean()
            
            if api_key.isalnum():
                
                with open(api_file, "w") as file:
                    
                    file.write(api_key)
                
                break
            
            else:
                
                tts("Le format de votre clé API Youtube est invalide, celle-ci doit être constituée uniquement de lettres et de chiffres !")
                messagebox.showerror(title="Youtube :", message="Le format de votre clé API Youtube est invalide, celle-ci doit être constituée uniquement de lettres et de chiffres !")
                
                os.remove(api_file)

    while True:
        
        youtube = build("youtube", "v3", developerKey=api_key)
        
        tts("Quel sujet souhaitez-vous que la vidéo aborde ?")
        subject = input("Quel sujet souhaitez-vous que la vidéo aborde ? : ")
        
        clean()
        
        tts("Combien de vidéos souhaitez-vous regarder ?")
        numbers_videos = input("Combien de vidéos souhaitez-vous regarder ? : ")
        
        clean()
        
        if numbers_videos.isdigit():
            
            pass
            
        elif not numbers_videos.isdigit() and int(numbers_videos) in range(0, 65536):
            
            tts("Veuillez entrer un chiffre ou un nombre compris entre 0 et 65535 !")
            messagebox.showerror(title="Youtube :", message="Veuillez entrer un chiffre ou un nombre compris entre 0 et 65535 !")
        
        try:
            
            request = youtube.search().list(
                
                q=subject,
                part="snippet",
                type="video",
                maxResults=numbers_videos,
            )
            
            response = request.execute()
           
            if "items" in response:
                
                for item in response["items"]:
                    
                    video_id = item["id"]["videoId"]
                    video_url = f"https://www.youtube.com/watch?v={video_id}"
                    
                    webbrowser.open_new_tab(video_url)
                
                tts("Souhaitez-vous rechercher d'autres vidéos ?")
                choice = input("Souhaitez-vous rechercher d'autres vidéos ? : ")
                
                clean()
                
                if "oui" in choice.lower():
                    
                    continue
                
                elif "non" in choice.lower():
                    
                    break
                
                else:
                    
                    tts("Veuillez choisir une option valide, par oui ou non !")
                    messagebox.showerror(title="Youtube :", message="Veuillez choisir une option valide, par oui ou non !")
                
        except googleapiclient.errors.HttpError:
            
            tts("Votre clé API Youtube est invalide, veuillez en transmettre une valide !")
            messagebox.showerror(title="Youtube :", message="Votre clé API Youtube est invalide, veuillez en transmettre une valide !")
            
            os.remove(api_file)
            
            ytb()

if __name__ == "__main__":
    
    ytb()