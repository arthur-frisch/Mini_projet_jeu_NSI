import tkinter as tk
from random import randint
import game

class fenetre(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Jeu !")
        self.geometry("1100x800")
        self.bg = tk.PhotoImage(file="plateau.png")
        self.label_test = tk.Label(self, image=self.bg)
        self.label_test.place(x=0, y=0)
        self.quit_button= tk.Button(self, text="Quitter", command=self.destroy)
        self.quit_button.place(x=350, y=750)
        self.frame_right_button = tk.Frame(self)
        self.frame_right_button.place(x=875, y=200)
        self.alea_button = tk.Button(self.frame_right_button, text="Lancer les dés", command=self.txt_output_modify)
        self.alea_button.pack()
        self.output_label = tk.Label(self.frame_right_button, text="Aucun nombre tiré.")
        self.output_label.pack(pady=5)
        self.button_test = tk.Button(self.frame_right_button, text="Test", command=self.affiche_carte_question)
        self.button_test.pack()
        self.mainloop()
    
    def txt_output_modify(self):
        nb = randint(1, 6)
        self.output_label.configure(text=f"Le nombre tiré est {nb}.")
        print(nb)
        
    def affiche_carte_question(self):
        cartes = game.affiche_carte("violettes", 20)
        self.carte_question = tk.PhotoImage(file=cartes[0])
        self.carte_reponse = tk.PhotoImage(file=cartes[1])
        self.label_image = tk.Label(self, image=self.carte_question)
        self.label_image.place(x=640, y=500)
        

        
fenetre()
