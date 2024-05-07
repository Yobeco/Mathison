from tkinter import *
import pygame
from PIL import ImageTk

# Variable qui témoigne de la couleur de la flêche

color = True   # True = Yellow  /  False = Blue


# Variable pour suivre l'état de la musique

music_state = "Stoped"     # "onPlay" / "Stoped" / "Paused"

# Fonctions pour gérer la musique

pygame.mixer.init()

# Charger le fichier
pygame.mixer.music.load("Medias/Madison.mp3")

def playOrPauseMusic():
    
    # Aller chercher l'indicateur d'état
    global music_state
    
    if music_state == "Stoped" :
        pygame.mixer.music.play()
        music_state = "onPlay"
        play_bouton.config(text="Pause")
        
    elif music_state == "Paused" :
        pygame.mixer.music.unpause()
        music_state = "onPlay"
        play_bouton.config(text="Pause")
        
    elif music_state == "onPlay" :
        pygame.mixer.music.pause()
        music_state = "Paused"
        play_bouton.config(text="Play")
        
    else :
        print("Error")

    print(music_state)
    

def stopMusic():
    global music_state
    pygame.mixer.music.stop()
    music_state = "Stoped"
    print(music_state)
    play_bouton.config(text="Play")

# Définition des fonctions associées aux touches : changement de l'image

def imgUp(event):
    global img
    global color
    if color == True:
        img = ImageTk.PhotoImage(file="Medias/Up-Y.png")
        color = not color
    else :
        img = ImageTk.PhotoImage(file="Medias/Up-B.png")
        color = not color
    label.config(image=img)

def imgDown(event):
    global img
    global color
    if color == True:
        img = ImageTk.PhotoImage(file="Medias/Down-Y.png")
        color = not color
    else :
        img = ImageTk.PhotoImage(file="Medias/Down-B.png")
        color = not color
    label.config(image=img)

def imgLeft(event):
    global img
    global color
    if color == True:
        img = ImageTk.PhotoImage(file="Medias/Left-Y.png")
        color = not color
    else :
        img = ImageTk.PhotoImage(file="Medias/Left-B.png")
        color = not color
    label.config(image=img)

def imgRight(event):
    global img
    global color
    if color == True:
        img = ImageTk.PhotoImage(file="Medias/Right-Y.png")
        color = not color
    else :
        img = ImageTk.PhotoImage(file="Medias/Right-B.png")
        color = not color
    label.config(image=img)

# Création de la fenêtre

fenetre = Tk()
fenetre.title("Mathison V0.2")

# frame 1
Frame1 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame1.pack(padx=10, pady=10)

# frame 2
Frame2 = Frame(fenetre, borderwidth=2)
Frame2.pack(padx=10, pady=10)

play_bouton=Button(Frame1, text="Play", command=playOrPauseMusic)
play_bouton.pack(side=LEFT)

stop_bouton=Button(Frame1, text="Stop", command=stopMusic)
stop_bouton.pack(side=LEFT)

img = ImageTk.PhotoImage(file="Medias/LogoMathison.png")
label = Label(Frame2, image=img)
label.pack()

# Lier la fonction changeImage à un événement clavier spécifique (par exemple, appuyer sur la touche "A")
fenetre.bind("<KeyPress-Up>", imgUp)
fenetre.bind("<KeyPress-Down>", imgDown)
fenetre.bind("<KeyPress-Left>", imgLeft)
fenetre.bind("<KeyPress-Right>", imgRight)

# Instanciation de la fenêtre

fenetre.mainloop()

