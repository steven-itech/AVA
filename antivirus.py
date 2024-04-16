import ctypes
import pyttsx3
import os
import hashlib
import requests
import subprocess
import wget
from fpdf import FPDF
from tkinter.filedialog import askopenfilename
from tkinter import messagebox

ctypes.windll.kernel32.SetConsoleTitleW("Antivirus :")

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def tts(message):
    
    engine.say(message)
    engine.runAndWait()

def clean():
    
    os.system("cls")

def antivirus():
    
    type_analyzes = """
    Avast = Effectuer une analyse antivirus via Avast.
    VirusTotal = Effectuer un scan d'un fichier, afin de savoir si celui-ci est malveillant ou non via l'API de VirusTotal !"""
    
    options = {
        
        "Avast": avast,
        "VirusTotal": virus_total,
    }

    for analyze in type_analyzes.strip().split("\n"):
        
        print(analyze.strip())

    tts("Quelle opération souhaitez-vous effectuer ?")
    choice = input("\n" + "Quelle opération souhaitez-vous effectuer ? : ")

    clean()
    
    if choice in options:
        
        options[choice]()
            
    else:
            
        tts("Veuillez choisir une option valide !")
        messagebox.showerror(title="Antivirus :", message="Veuillez choisir une option valide !")
        
        antivirus()
              
def avast():
    
    tts("Souhaitez-vous effectuer une analyse antivirus avec Avast ?")
    avast_choice = input("Souhaitez-vous effectuer une analyse antivirus avec Avast ? : ")
    
    clean()

    if "oui" in avast_choice.lower():
       
        tts("Souhaitez-vous effectuer une analyse d'un lecteur ou de votre système ?")
        type_analysis = input("Quelle analyse souhaitez-vous effectuer ? : ")
        
        clean()

        avast_path = r"C:\Program Files\AVAST Software\Avast"

        if os.path.exists(avast_path):
            
            os.chdir(avast_path)

            if "lecteur" in type_analysis.lower():
                
                tts("Quelle est la lettre du lecteur à analyser ?")
                drive = input("Quelle est la lettre du lecteur à analyser ? : ")
                
                clean()
                
                subprocess.run(["ashCmd.exe", drive])

            elif "système" in type_analysis.lower():
                
                subprocess.run(["ashCmd.exe", "C:"])

            else:
                
                tts("Vous ne possédez pas Avast, souhaitez-vous le télécharger et l'installer afin de procéder à l'analyse ?")
                install = input("Souhaitez-vous télécharger et installer Avast, afin de procéder à l'analyse ? : ")
                
                clean()

                if "oui" in install.lower():
                    
                    url = "https://www.avast.com/fr-fr/download-thank-you.php?product=PRW-ONLINE-PP&locale=fr-fr&direct=1"
                    wget.download(url)
                    
                elif "non" in install:
                    
                    antivirus()

    elif "non" in avast_choice:
        
        antivirus()
        
    else:
        
        tts("Veuillez choisir une option valide, par oui ou non !")
        messagebox.showerror(title="Antivirus :", message="Veuillez choisir une option valide, par oui ou par non !")

def virus_total():
    
    url = "https://www.virustotal.com/api/v3/files"

    try:
        
        api_file = "api-virustotal.txt"
       
        with open(api_file, "r") as file:
            
            api_key = file.readline().strip()
    
    except FileNotFoundError:
       
        while True:
            
            tts("Quelle est votre clé API VirusTotal ?")
            api_key = input("Veuillez transmettre votre clé API VirusTotal : ")
            
            clean()
            
            if api_key.isalnum():
               
                with open(api_file, "w") as file:
                    
                    file.write(api_key)
               
                break
            
            else:
                
                tts("Le format de votre clé API VirusTotal est invalide, celle-ci doit être constituée uniquement de lettres et de chiffres !")
                messagebox.showerror(title="Antivirus :", message="Le format de votre clé API VirusTotal est invalide, celle-ci doit être constituée uniquement de lettres et de chiffres !")
                
                os.remove(api_file)
                
                virus_total()

    tts("Veuillez choisir le fichier à analyser !")
    file_path = askopenfilename()

    while not file_path.endswith(".exe"):
        
        tts("Veuillez choisir uniquement un fichier exécutable !")
        messagebox.showerror(title="Antivirus :", message="Veuillez choisir uniquement un fichier exécutable !")
        
        file_path = askopenfilename()

    with open(file_path, "rb") as file:
        
        file_content = file.read()
        file_hash = hashlib.sha256(file_content).hexdigest()

    url += "/" + file_hash
    headers = {
        
        "accept": "application/json",
        "x-apikey": api_key
    }

    try:
       
        response = requests.get(url, headers=headers)
        response.raise_for_status()  
        
        result_json = response.json() 
    
    except requests.exceptions.RequestException:
        
        tts("Votre clé API VirusTotal est invalide, veuillez en transmettre une valide !")
        messagebox.showerror(title="Antitivurs :", message="Votre clé API VirusTotal est invalide, veuillez en transmettre une valide !")
        
        os.remove(api_file)
       
        antivirus()

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=10)

    pdf.cell(200,10, txt="Compte rendu de l'analyse antivirus : ", ln = True, align = "C")

    malicious_count = 0

    for analysis, data in result_json["data"]["attributes"]["last_analysis_results"].items():
        
        if data["result"] is not None:
            
            malicious_count += 1
        
        if data["result"] is None:
            
            result = "Non malveillant !"
        
        else:
            
            result = data["result"]
        
        pdf.cell(200, 10, txt=f"{analysis}: {result}", ln=True, align="L")

    if malicious_count == 0:
        
        tts("Le fichier n'est pas malveillant !")
        messagebox.showinfo(title="Antivirus :", message="Le fichier n'est pas malveillant !")
        
        note = "Le fichier n'est pas malveillant !"
    
    elif malicious_count < 5:
       
        tts("Le fichier est potentiellement malveillant, par mesure de sécurité, veuillez ne pas l'exécuter !")
        messagebox.showwarning(title="Antivirus :", message="Le fichier est potentiellement malveillant, par mesure de sécurité, veuillez ne pas l'exécuter !")
        
        note = "Le fichier est potentiellement malveillant, par mesure de sécurité, veuillez ne pas l'exécuter !"
    
    else:
        
        tts("Le fichier est malveillant, veuillez le supprimer manuellement afin de préserver l'intégrité de votre ordinateur et de vos données !")
        messagebox.showwarning(title="Antivirus :", message="Le fichier est malveillant, veuillez le supprimer manuellement afin de préserver l'intégrité de votre ordinateur et de vos données !")
        
        note = "Le fichier est malveillant, veuillez le supprimer manuellement afin de préserver l'intégrité de votre ordinateur et de vos données !"

    pdf.set_font("Arial", size=6)
    pdf.cell(200, 10, txt=f"Conclusion en fonction du nombre de détections malveillantes des antivirus : {note}", ln=True, align="L")

    tts("Veuillez transmettre le nom que vous souhaitez attribuer au PDF !")
    pdf_name = input("Veuillez transmettre le nom que vous souhaitez attribuer au PDF : ")
    
    clean()

    while not pdf_name.isalpha():
        
        tts("Veuillez choisir un nom constitué uniquement de lettres !")
        messagebox.showerror(title="Antivirus :", message="Veuillez choisir un nom constitué uniquement de lettres !")
        
        pdf_name = input("Veuillez transmettre le nom que vous souhaitez attribuer au PDF : ")
        
        clean()

    pdf.output(pdf_name + ".pdf")

    tts("Le compte rendu de l'analyse antivirus vient d'être créé !")
    messagebox.showinfo(title="Antivirus :", message="Le compte rendu de l'analyse antivirus vient d'être créé !")
    
    antivirus()

if __name__ == "__main__":
    
    antivirus()