from tkinter import *
import pygame
from PIL import ImageTk

pygame.mixer.init()
pygame.mixer.music.load("Medias/Madison.mp3")
pygame.mixer.music.play()

fenetre = Tk()

# frame 1
Frame1 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame1.pack(padx=10, pady=10)

# frame 2
Frame2 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame2.pack(padx=10, pady=10)

# frame 3
Frame3 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame3.pack(padx=10, pady=10)

label = Label(Frame1, text="Mathison")
label.pack()

play_bouton=Button(Frame2, text="Play", command=None)
play_bouton.pack(side=LEFT)

stop_bouton=Button(Frame2, text="Stop", command=None)
stop_bouton.pack(side=LEFT)

img = ImageTk.PhotoImage(file="Medias/LogoMathison.png")
label = Label(Frame3, image=img)
label.pack()


fenetre.mainloop()

