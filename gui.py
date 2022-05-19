import tkinter as tk
import game

class Fenetre(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pop sauce")
        self.geometry("900x500")

        # Frame de base
        self.start_frame = tk.Frame(self)
        self.start_frame.pack()
        self.start_label = tk.Label(self.start_frame, text="Bienvenue sur notre jeu dénommé Pop Sauce !\n\nLe principe du jeu est très simple, dans le mode en ligne, vous pourrez affronter un ami à travers\n différentes questions chacun votre tour. Celui qui obtient le plus de points gagne !\n\nDans le mode local, vous pourrez choisir le nombre de questions à traiter. Le but est ici\n d'avoir le plus de points possible à la fin du jeu.\n\n  Veuillez choisir une option !", font=("Arial", 15))
        self.start_label.pack()
        
        # Bouton "online game"
        self.image_online_game_button = tk.PhotoImage(file="online_game_button.gif")
        self.start_button_online = tk.Button(self.start_frame, image=self.image_online_game_button, borderwidth=0, command=self.online_first_step, text="online game", font=("Arial", 10))
        self.start_button_online.pack(pady=20)
        
        # Bouton "local game"
        self.image_local_game_button = tk.PhotoImage(file="local_game_button.gif")
        self.start_button = tk.Button(self.start_frame, image=self.image_local_game_button, borderwidth=0, command=self.local_step, text="local game", font=("Arial", 10))
        self.start_button.pack()
        
        # Bouton "quit"
        self.image_quit_game_button = tk.PhotoImage(file="quit_game_button.gif")
        self.start_button_quit = tk.Button(self.start_frame, image=self.image_quit_game_button, borderwidth=0, command=self.destroy, text="quit", font=("Arial", 10))
        self.start_button_quit.pack(pady=20)
        
        self.mainloop()
        
    def local_step(self):
        """Méthode renvoyant l'utilisateur sur le menu lui permettant de choisir le nombre de questions souhaitées
        """
        self.start_frame.destroy()
        self.geometry("1100x400")
        self.frame_local_step = tk.Frame(self)
        self.frame_local_step.pack()
        self.label_local_step = tk.Label(self.frame_local_step, text="Vous pouvez choisir le nombre de questions souhaitées :", font=("Arial", 15))
        self.label_local_step.pack()
        
        # Bouton "10 questions"
        self.image_10questions_button = tk.PhotoImage(file="10questions_button.gif")
        self.button10 = tk.Button(self.frame_local_step, image=self.image_10questions_button, borderwidth=0, command=lambda: self.local_step_2(10), text="10 questions", font=("Arial", 15))
        self.button10.pack(pady=40)
        
        # Bouton "20 questions"
        self.image_20questions_button = tk.PhotoImage(file="20questions_button.gif")
        self.button20 = tk.Button(self.frame_local_step, image=self.image_20questions_button, borderwidth=0, command=lambda: self.local_step_2(20), text="20 questions", font=("Arial", 15))
        self.button20.pack()
        
        # Bouton "30 questions"
        self.image_30questions_button = tk.PhotoImage(file="30questions_button.png")
        self.button30 = tk.Button(self.frame_local_step, image=self.image_30questions_button, borderwidth=0, command=lambda: self.local_step_2(30) , text="30 questions", font=("Arial", 15))
        self.button30.pack(pady=40)
        
    def local_step_2(self, nb : int):
        """Méthode passant l'utilisateur du menu 1 au jeu principal en local

        Args:
            nb (int): nombre de questions voulant être traitées par l'utilisateur
        """
        self.frame_local_step.destroy()
        self.nb_question = nb
        self.nb_total_question = nb
        self.nb_good_answer = 0
        self.main_frame = tk.Frame(self)
        self.main_frame.pack()
        self.question = game.question()
        self.main_label = tk.Label(self.main_frame, text=self.question[1], font=("Arial", 15))
        self.main_label.pack()
        self.main_entry = tk.Entry(self.main_frame, width=35, font=("Arial", 15))
        self.main_entry.pack(pady=120)
        self.reponse_label = tk.Label(self.main_frame, bd=5, font=("Arial", 15))
        self.reponse_label.pack()
        self.button_next_question = tk.Button(self.main_frame, command=self.next_question, text="Envoie la réponse", width=25, font=("Arial", 15))
        self.button_next_question.pack()

    def next_question(self):
        """Méthode permettant de passer d'une question à la suivante
        """
        self.answer = self.main_entry.get()
        self.main_entry.delete(0, tk.END)
        self.nb_question -= 1
        if game.comparaison_levenshtein(self.question[2], self.answer) < 4:
            self.reponse_label.configure(text="Bien joué, bonne réponse !")
            self.nb_good_answer += 1
        else:
            self.reponse_label.configure(text=f"Dommage, mauvaise réponse ! La réponse était \"{self.question[2]}\".")
    
            
        if self.nb_question != 0:
            self.question = game.question()
            self.main_label.configure(text=self.question[1])
        else:
            self.main_frame.destroy()
            self.end_frame = tk.Frame(self)
            self.end_frame.pack()
            self.end_label = tk.Label(self.end_frame, text=f"Vous avez fait un score de {self.nb_good_answer}/{self.nb_total_question} !", font=("Arial", 15))
            self.end_label.pack()
            self.end_button_restart = tk.Button(self.end_frame, command=self.restart, text="Recommencer", width=25)
            self.end_button_restart.pack(pady=35)
            self.end_button_menu = tk.Button(self.end_frame, command=self.menu, text="Retour au menu", width=25)
            self.end_button_menu.pack()
            self.end_button_quit = tk.Button(self.end_frame, command=self.destroy, text="Quitter", width=25)
            self.end_button_quit.pack(pady=35)
            
        
    def restart(self):
        """Méthode renvoyant l'utilisateur au menu local lui permettant de chosir le nombre de questions
        """
        self.end_frame.destroy()
        self.local_step()
        
    def menu(self):
        """Méthode renvoyant l'utilisateur au menu principal
        """
        self.end_frame.destroy()
        self.geometry("900x500")

        # Frame de base
        self.start_frame = tk.Frame(self)
        self.start_frame.pack()
        self.start_label = tk.Label(self.start_frame, text="Bienvenue sur notre jeu dénommé Pop Sauce !\n\nLe principe du jeu est très simple, dans le mode en ligne, vous pourrez affronter un ami à travers\n différentes questions. Celui qui obtient le plus de points gagne !\n\nDans le mode local, vous pourrez choisir le nombre de questions à traiter. Le but est ici\n d'avoir le plus de points possible à la fin du jeu.\n\n  Veuillez choisir une option !", font=("Arial", 15))
        self.start_label.pack()
        
        # Bouton "online game"
        self.image_online_game_button = tk.PhotoImage(file="online_game_button.gif")
        self.start_button_online = tk.Button(self.start_frame, image=self.image_online_game_button, borderwidth=0, command=self.online_first_step, text="online game", font=("Arial", 10))
        self.start_button_online.pack(pady=20)
        
        # Bouton "local game"
        self.image_local_game_button = tk.PhotoImage(file="local_game_button.gif")
        self.start_button = tk.Button(self.start_frame, image=self.image_local_game_button, borderwidth=0, command=self.local_step, text="local game", font=("Arial", 10))
        self.start_button.pack()
        
        # Bouton "quit"
        self.image_quit_game_button = tk.PhotoImage(file="quit_game_button.gif")
        self.start_button_quit = tk.Button(self.start_frame, image=self.image_quit_game_button, borderwidth=0, command=self.destroy, text="quit", font=("Arial", 10))
        self.start_button_quit.pack(pady=20)
        
    def online_first_step(self):
        """Méthode permettant au joueur de démarrer une partie en ligne
        """
        self.start_frame.destroy()
        self.geometry("1100x400")
        self.online_first_step_frame = tk.Frame(self)
        self.online_first_step_frame.pack()
        self.online_first_step_label = tk.Label(self.online_first_step_frame, font = ("Arial", 15), text="Pseudo joueur 1 :")
        self.online_first_step_label.pack()
        self.online_first_step_entry = tk.Entry(self.online_first_step_frame, font = ("Arial", 15))
        self.online_first_step_entry.pack(pady=15)
        self.online_first_step_label2 = tk.Label(self.online_first_step_frame, font = ("Arial", 15), text="Pseudo joueur 2 :")
        self.online_first_step_label2.pack()
        self.online_first_step_entry2 = tk.Entry(self.online_first_step_frame, font = ("Arial", 15))
        self.online_first_step_entry2.pack(pady=15)
        self.online_first_step_button = tk.Button(self.online_first_step_frame, text="Commencer le jeu !", font = ("Arial", 15), command=self.online_second_step)
        self.online_first_step_button.pack()
        
    def online_second_step(self):
        """_summary_
        """
        self.nb_question = 20
        self.nb_question_total = 20
        self.pseudo_joueur1 = self.online_first_step_entry.get()
        self.joueur1_good_answer = 0
        self.pseudo_joueur2 = self.online_first_step_entry2.get()
        self.joueur2_good_answer = 0
        self.online_first_step_frame.destroy()
        self.online_second_step_frame = tk.Frame(self)
        self.online_second_step_frame.pack()
        self.question = game.question()
        self.label_question = tk.Label(self.online_second_step_frame, text=f"{self.question[1]}\n{self.pseudo_joueur1}, à vous !", font=("Arial", 15))
        self.label_question.pack()
        self.online_second_step_entry = tk.Entry(self.online_second_step_frame, font=("Arial", 15))
        self.online_second_step_entry.pack()
        self.online_second_step_label_reponse = tk.Label(self.online_second_step_frame)
        self.online_second_step_label_reponse.pack()
        self.online_second_step_button = tk.Button(self.online_second_step_frame, command=self.next_question_online, text="Prochaine question")
        self.online_second_step_button.pack()
        
    def next_question_online(self):
        """_summary_
        """
        self.nb_question -= 1
        self.tour_joueur = self.nb_question % 2
        self.answer = self.online_second_step_entry.get()
        self.online_second_step_entry.delete(0, tk.END)
        if game.comparaison_levenshtein(self.question[2], self.answer) < 4:
            self.online_second_step_label_reponse.configure(text="Bien joué bonne réponse")
            if self.tour_joueur == 0:
                self.joueur2_good_answer += 1
            else:
                self.joueur1_good_answer += 1
        else:
            self.online_second_step_label_reponse.configure(text=f"Dommage, la réponse était \"{self.question[2]}\"")
        self.question = game.question()
        if self.tour_joueur == 0:
            self.label_question.configure(text=f"{self.question[1]}\n{self.pseudo_joueur1}, à vous !")
        else:
            self.label_question.configure(text=f"{self.question[1]}\n{self.pseudo_joueur2}, à vous !")
        
        if self.nb_question == 0:
            self.online_second_step_frame.destroy()
            self.online_last_frame = tk.Frame(self)
            self.online_last_frame.pack()
            if self.joueur1_good_answer < self.joueur2_good_answer:
                self.online_last_label = tk.Label(self.online_last_frame, text=f"{self.pseudo_joueur2} gagne avec {self.joueur2_good_answer} points. {self.pseudo_joueur1} s'est néanmoins bien battu avec {self.joueur1_good_answer} points !", font=("Arial", 15))
            elif self.joueur1_good_answer > self.joueur2_good_answer:
                self.online_last_label = tk.Label(self.online_last_frame, text=f"{self.pseudo_joueur1} gagne avec {self.joueur1_good_answer} points. {self.pseudo_joueur2} s'est néanmoins bien battu avec {self.joueur2_good_answer} points !", font=("Arial", 15))
            else:
                self.online_last_label = tk.Label(self.online_last_frame, text=f"{self.pseudo_joueur1} et {self.pseudo_joueur2}, vous êtes à égalité avec {self.joueur2_good_answer} points.", font=("Arial", 15))
            self.online_last_label.pack()
            self.end_button_restart = tk.Button(self.online_last_frame, command=self.restart2, text="Recommencer", width=25)
            self.end_button_restart.pack(pady=35)
            self.end_button_menu = tk.Button(self.online_last_frame, command=self.menu2, text="Retour au menu", width=25)
            self.end_button_menu.pack()
            self.end_button_quit = tk.Button(self.online_last_frame, command=self.destroy, text="Quitter", width=25)
            self.end_button_quit.pack(pady=35)
            
    def menu2(self):
        """Méthode renvoyant l'utilisateur au menu principal
        """
        self.online_last_frame.destroy()
        self.geometry("900x500")

        # Frame de base
        self.start_frame = tk.Frame(self)
        self.start_frame.pack()
        self.start_label = tk.Label(self.start_frame, text="Bienvenue sur notre jeu dénommé Pop Sauce !\n\nLe principe du jeu est très simple, dans le mode en ligne, vous pourrez affronter un ami à travers\n différentes questions. Celui qui obtient le plus de points gagne !\n\nDans le mode local, vous pourrez choisir le nombre de questions à traiter. Le but est ici\n d'avoir le plus de points possible à la fin du jeu.\n\n  Veuillez choisir une option !", font=("Arial", 15))
        self.start_label.pack()
        
        # Bouton "online game"
        self.image_online_game_button = tk.PhotoImage(file="online_game_button.gif")
        self.start_button_online = tk.Button(self.start_frame, image=self.image_online_game_button, borderwidth=0, command=self.online_first_step, text="online game", font=("Arial", 10))
        self.start_button_online.pack(pady=20)
        
        # Bouton "local game"
        self.image_local_game_button = tk.PhotoImage(file="local_game_button.gif")
        self.start_button = tk.Button(self.start_frame, image=self.image_local_game_button, borderwidth=0, command=self.local_step, text="local game", font=("Arial", 10))
        self.start_button.pack()
        
        # Bouton "quit"
        self.image_quit_game_button = tk.PhotoImage(file="quit_game_button.gif")
        self.start_button_quit = tk.Button(self.start_frame, image=self.image_quit_game_button, borderwidth=0, command=self.destroy, text="quit", font=("Arial", 10))
        self.start_button_quit.pack(pady=20)
    
    def restart2(self):
        """Méthode renvoyant l'utilisateur au menu local lui permettant de chosir le nombre de questions
        """
        self.online_last_frame.destroy()
        self.online_first_step()
        
Fenetre()
