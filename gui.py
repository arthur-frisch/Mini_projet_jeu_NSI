import tkinter as tk
from random import randint


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
        self.frame_right_button.place(x=750, y=350)
        self.alea_button = tk.Button(self.frame_right_button, text="Test", command=self.destroy)
        self.alea_button.pack()
        self.alea_button2 = tk.Button(self.frame_right_button, text="Test", command=self.destroy)
        self.alea_button2.pack()
        self.mainloop()
        

        
fenetre()
