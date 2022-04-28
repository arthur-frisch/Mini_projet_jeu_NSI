import tkinter as tk
from random import randint

def nb_alea():
    text.set("Nombre : " + str(randint(1,6)))
    

fenetre = tk.Tk()
text = tk.StringVar()
text.set("Test")
textlabel = tk.Label(fenetre, textvariable=text)
textlabel.pack()
canvas = tk.Canvas(width=500, height=500)
canvas.pack()
bouton = tk.Button(fenetre, command=nb_alea, width=8, height=1, text="Tirage nb")
bouton.pack()
fenetre.mainloop()