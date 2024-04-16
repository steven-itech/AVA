import vlc
import tkinter as tk
import os
from tkinter import ttk

#Dictionnaire comportant l'ensemble des flux radios.
radios = {
    
    "NRJ Afro": "http://cdn.nrjaudio.fm/adwz1/fr/57770/mp3_128.mp3?origine=fluxradios&aw_0_1st.station=NRJ-Afro-Hits",
    "NRJ RAP": "https://scdn.nrjaudio.fm/adwz1/fr/55189/mp3_128.mp3?origine=fluxradios&aw_0_1st.station=NRJ-Classic-Rap-FR",
    "NRJ RAP US": "https://scdn.nrjaudio.fm/adwz1/fr/31093/mp3_128.mp3?origine=fluxradios&aw_0_1st.station=NRJ-Classic-Rap-US",
    "NRJ RNB": "https://scdn.nrjaudio.fm/adwz1/fr/31095/mp3_128.mp3?origine=fluxradios&aw_0_1st.station=NRJ-Classic-RnB",
    "NRJ ROCK": "https://scdn.nrjaudio.fm/adwz1/fr/31097/mp3_128.mp3?origine=fluxradios&aw_0_1st.station=NRJ-Classic-Rock",
    "NRJ CLUB": "https://scdn.nrjaudio.fm/adwz1/fr/31073/mp3_128.mp3?origine=fluxradios&aw_0_1st.station=NRJ-Club-Hits",
    "NRJ DAVID GUETTA": "https://scdn.nrjaudio.fm/audio1/fr/31053/mp3_128.mp3?origine=fluxradios",
    "NRJ DEEP": "https://scdn.nrjaudio.fm/adwz1/fr/31437/mp3_128.mp3?origine=fluxradios&aw_0_1st.station=NRJ-Deep",
    "NRJ DISNEY": "https://scdn.nrjaudio.fm/adwz1/fr/56896/mp3_128.mp3?origine=fluxradios&aw_0_1st.station=NRJ-Disney-Hits",
    "NRJ EDM": "https://scdn.nrjaudio.fm/adwz1/fr/31419/mp3_128.mp3?origine=fluxradios&aw_0_1st.station=NRJ-EDM",
    "NRJ EUROHOT": "https://scdn.nrjaudio.fm/adwz1/fr/31407/mp3_128.mp3?origine=fluxradios&aw_0_1st.station=NRJ-Eurohot-30",
    "NRJ EXTRA": "https://scdn.nrjaudio.fm/adwz1/fr/30027/mp3_128.mp3?origine=fluxradios&aw_0_1st.station=NRJ-Extravadance",
    "NRJ FIESTA": "https://scdn.nrjaudio.fm/adwz1/fr/31247/mp3_128.mp3?origine=fluxradios&aw_0_1st.station=NRJ-Fiesta",
    "NRJ FIESTA LATINA": "https://scdn.nrjaudio.fm/adwz1/fr/55210/mp3_128.mp3?origine=fluxradios&aw_0_1st.station=NRJ-Fiesta-Latina",
    "NRJ FRENCH": "https://scdn.nrjaudio.fm/adwz1/fr/30037/mp3_128.mp3?origine=fluxradios&aw_0_1st.station=NRJ-French-Hits",
    "NRJ FUNKY": "https://scdn.nrjaudio.fm/adwz1/fr/31035/mp3_128.mp3?origine=fluxradios&aw_0_1st.station=NRJ-Funky",
    "NRJ HARD": "https://scdn.nrjaudio.fm/adwz1/fr/56708/mp3_128.mp3?origine=fluxradios&aw_0_1st.station=NRJ-Hardstyle",
    "NRJ IBIZA": "https://scdn.nrjaudio.fm/adwz1/fr/30031/mp3_128.mp3?origine=fluxradios&aw_0_1st.station=NRJ-Ibiza",
    "NRJ LATINO": "https://scdn.nrjaudio.fm/adwz1/fr/30077/mp3_128.mp3?origine=fluxradios&aw_0_1st.station=NRJ-Latino",
    "NRJ LOVE": "https://scdn.nrjaudio.fm/adwz1/fr/30081/mp3_128.mp3?origine=fluxradios&aw_0_1st.station=NRJ-Love",
    "NRJ FRANCE": "https://scdn.nrjaudio.fm/adwz1/fr/31217/mp3_128.mp3?origine=fluxradios&aw_0_1st.station=Made-In-France",
    "NRJ METAL": "https://scdn.nrjaudio.fm/adwz1/fr/30079/mp3_128.mp3?origine=fluxradios&aw_0_1st.station=NRJ-Metal",
    "NRJ POP": "https://scdn.nrjaudio.fm/adwz1/fr/30053/mp3_128.mp3?origine=fluxradios&aw_0_1st.station=NRJ-Pop",
    "NRJ POP RNB": "https://scdn.nrjaudio.fm/adwz1/fr/31489/mp3_128.mp3?origine=fluxradios&aw_0_1st.station=NRJ-Pop-Rnb-Dance",
    "NRJ POP URBAINE": "https://scdn.nrjaudio.fm/adwz1/fr/55764/mp3_128.mp3?origine=fluxradios&aw_0_1st.station=NRJ-Pop-Urbaine",
    "NRJ POUR LE SPORT": "https://scdn.nrjaudio.fm/adwz1/fr/55513/mp3_128.mp3?origine=fluxradios&aw_0_1st.station=NRJ-Pour-Le-Sport",
    "NRJ RELAX": " https://scdn.nrjaudio.fm/adwz1/fr/31161/mp3_128.mp3?origine=fluxradios&aw_0_1st.station=NRJ-Relax",
    "NRJ SENTIMENTAL": "https://scdn.nrjaudio.fm/adwz1/fr/31277/mp3_128.mp3?origine=fluxradios&aw_0_1st.station=NRJ-Sentimental",
    
    "NRJ SPORT": "https://scdn.nrjaudio.fm/adwz1/fr/57904/mp3_128.mp3?origine=fluxradios&aw_0_1st.station=NRJ-Sport-Motivation",
    "NOSTALGIE HUMEUR": "https://scdn.nrjaudio.fm/adwz1/fr/55678/mp3_128.mp3?origine=fluxradios&aw_0_1st.station=Nostalgie-Bonne-Humeur",
    "NOSTALGIE CINÉ": "https://scdn.nrjaudio.fm/adwz1/fr/55678/mp3_128.mp3?origine=fluxradios&aw_0_1st.station=Nostalgie-Bonne-Humeur",
    "NOSTALGIE DISCO": "https://scdn.nrjaudio.fm/adwz1/fr/30617/mp3_128.mp3?origine=fluxradios&aw_0_1st.station=Nostalgie-Disco",
    "NOSTALGIE FUNK": "https://scdn.nrjaudio.fm/adwz1/fr/30607/mp3_128.mp3?origine=fluxradios&aw_0_1st.station=Nostalgie-Funk",  
    "NOSTALGIE ITALIA": "https://scdn.nrjaudio.fm/adwz1/fr/30663/mp3_128.mp3?origine=fluxradios&aw_0_1st.station=Nostalgie-Italia",
    "NOSTALGIE ITALO": "https://scdn.nrjaudio.fm/adwz1/fr/58333/mp3_128.mp3?origine=fluxradios&aw_0_1st.station=Nostalgie-Italo-Disco",
    "NOSTALGIE JAZZ": "https://scdn.nrjaudio.fm/adwz1/fr/30641/mp3_128.mp3?origine=fluxradios&aw_0_1st.station=Nostalgie-Jazz",
    "NOSTALGIE JOHNNY HALLYDAY": "http://cdn.nrjaudio.fm/audio1/fr/30713/mp3_128.mp3?origine=fluxradios",
    "NOSTALGIE LÉGENDES": "https://scdn.nrjaudio.fm/adwz1/fr/55196/mp3_128.mp3?origine=fluxradios&aw_0_1st.station=Nostalgie-Legendes",
    "NOSTALGIE MAXI": "https://scdn.nrjaudio.fm/adwz1/fr/56937/mp3_128.mp3?origine=fluxradios&aw_0_1st.station=Nostalgie-Maxi-45-T",
    "NOSTALGIE MINI": "https://scdn.nrjaudio.fm/adwz1/fr/56955/mp3_128.mp3?origine=fluxradios&aw_0_1st.station=Nostalgie-Mini-Mix",
    "NOSTALGIE ROCK": "https://scdn.nrjaudio.fm/adwz1/fr/30621/mp3_128.mp3?origine=fluxradios&aw_0_1st.station=Nostalgie-Rock",
    "NOSTALGIE ROUTE": "https://scdn.nrjaudio.fm/adwz1/fr/56040/mp3_128.mp3?origine=fluxradios&aw_0_1st.station=Nostalgie-Route-66",
    "NOSTALGIE SATURDAY": "https://scdn.nrjaudio.fm/adwz1/fr/30773/mp3_128.mp3?origine=fluxradios&aw_0_1st.station=Nostalgie-Saturday-Night",
    "NOSTALGIE SLOW": "https://scdn.nrjaudio.fm/adwz1/fr/58004/mp3_128.mp3?origine=fluxradios&aw_0_1st.station=Nostalgie-Slow-80",
    "NOSTALGIE SOUL": " https://scdn.nrjaudio.fm/adwz1/fr/56953/mp3_128.mp3?origine=fluxradios&aw_0_1st.station=Nostalgie-Soul",
    "NOSTALGIE FRANCAIS": "https://scdn.nrjaudio.fm/adwz1/fr/30611/mp3_128.mp3?origine=fluxradios&aw_0_1st.station=Nostalgie-Tubes-Francais",
    "NOSTALGIE USA": "https://scdn.nrjaudio.fm/adwz1/fr/56621/mp3_128.mp3?origine=fluxradios&aw_0_1st.station=Nostalgie-USA-80",
    
}

player = None  

#Fonction qui permet de jouer la radio.
def play_radio():
    
    global player
    
    radio_choice = radio_var.get()
    
    if radio_choice in radios:
        
        if player is not None:
            
            player.stop()
        
        instance = vlc.Instance()
        media = instance.media_new(radios[radio_choice])
        
        player = instance.media_player_new()
        player.set_media(media)
        player.play()
        
        os.system("cls")

#Fonction qui permet d'arrêter la radio.
def stop_radio():
    
    global player
    
    if player is not None:
        
        player.stop()

root = tk.Tk()
root.title("Radio :")

main_frame = ttk.Frame(root, padding="30")
main_frame.grid(row=0, column=0)

title_label = ttk.Label(main_frame, text="Écoutez votre radio préférée :", font=("Helvetica", 20))
title_label.grid(row=0, column=0, columnspan=2, pady=10)

radio_label = ttk.Label(main_frame, text="Choisissez votre radio :", font=("Helvetica", 12))
radio_label.grid(row=1, column=0, padx=10, pady=5)

radio_var = tk.StringVar(root)
radio_var.set(list(radios.keys())[0])  

radio_menu = ttk.OptionMenu(main_frame, radio_var, *radios.keys())
radio_menu.grid(row=1, column=1, padx=10, pady=5)

play_button = ttk.Button(main_frame, text="Écouter !", command=play_radio)
play_button.grid(row=2, column=0, pady=10, padx=5, sticky="e")

stop_button = ttk.Button(main_frame, text="Arrêter !", command=stop_radio)
stop_button.grid(row=2, column=1, pady=10, padx=5, sticky="w")

root.mainloop()