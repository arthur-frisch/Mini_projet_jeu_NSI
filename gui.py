import tkinter as tk
from random import randint


class fenetre:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Trivial Poursuit")
        self.window.geometry("1100x900")
        self.bg = Bg(self.window)
        self.frame = Frame(self.window)
        self.window.mainloop()

class Button:
    def __init__(self, window, _text : str, _command=None):
        self.button = tk.Button(window, text=_text, fg="black", command=_command)
        self.button.pack()

        
class Bg:
    def __init__(self, frame):
        self.bg = tk.PhotoImage(file="plateau.png")
        self.label = tk.Label(frame, image=self.bg)
        self.label.pack()
        
class Frame:
    def __init__(self, window):
        self.frame = tk.Frame(window)
        self.frame.pack()
        self.button = Button(self.frame, "Destruction", window.destroy)
        
    def test(self):
        print("Test ")
    
        
fenetre()
