import sqlite3
from random import shuffle

list_nb_bleues = list(range(1, 11))
list_nb_vertes = list(range(11, 21))
list_nb_oranges = list(range(21, 31))
list_nb_violettes = list(range(31, 41))
list_nb_roses = list(range(41, 51))
list_nb_jaunes = list(range(51, 61))
shuffle(list_nb_bleues)
shuffle(list_nb_vertes)
shuffle(list_nb_oranges)
shuffle(list_nb_violettes)
shuffle(list_nb_roses)
shuffle(list_nb_jaunes)

class Camembert:
    def __init__(self):
        self.camembert = []
        
    def is_win(self):
        tab=["Bleu", "Rose", "Jaune", "Violet", "Vert", "Orange"]
        for i in tab:
            if i not in self.camembert:
                return False
        return True

def comparaison_levenshtein(mot1 : str, mot2 : str):
    """_summary_

    Args:
        str1 (str): _description_
        str2 (str): _description_
    """
    mot1 = mot1.lower()
    mot2 = mot2.lower()
    mot1 = "".join(x for x in mot1 if x not in " " and x not in "'")
    mot2 = "".join(x for x in mot2 if x not in " " and x not in "'")
    
    ligne_i = [k for k in range(len(mot1)+1)]
    for i in range(1, len(mot2) + 1):
        ligne_prec = ligne_i
        ligne_i = [i]*(len(mot1)+1)
        for k in range(1,len(ligne_i)):
            cout = int(mot1[k-1] != mot2[i-1])
            ligne_i[k] = min(ligne_i[k-1] + 1, ligne_prec[k] + 1, ligne_prec[k-1] + cout)
    return ligne_i[len(mot1)]
    
def question(color : str):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    if color == "vertes":
        nb = list_nb_vertes[0]
        del(list_nb_vertes[0])
        request = c.execute(f"SELECT * FROM cartes WHERE id={nb} AND couleur='{color}'")
        
    elif color == "bleues":
        nb = list_nb_bleues[0]
        del(list_nb_bleues[0])
        request = c.execute(f"SELECT * FROM cartes WHERE id={nb} AND couleur='{color}'")
    
    elif color == "oranges":
        nb = list_nb_oranges[0]
        del(list_nb_oranges[0])
        request = c.execute(f"SELECT * FROM cartes WHERE id={nb} AND couleur='{color}'")
    
    elif color == "violettes":
        nb = list_nb_violettes[0]
        del(list_nb_violettes[0])
        request = c.execute(f"SELECT * FROM cartes WHERE id={nb} AND couleur='{color}'")
    
    elif color == "roses":
        nb = list_nb_roses[0]
        del(list_nb_roses[0])
        request = c.execute(f"SELECT * FROM cartes WHERE id={nb} AND couleur='{color}'") 
    
    elif color == "jaunes":
        nb = list_nb_jaunes[0]
        del(list_nb_jaunes[0])
        request = c.execute(f"SELECT * FROM cartes WHERE id={nb} AND couleur='{color}'")
        
    request = request.fetchall()[0]
    conn.close()
    return (request[2], nb)

def affiche_carte(color : str, nb : int):
    """_summary_

    Args:
        color (_type_): _description_
    """
    color = color.upper()
    nb %= 10
    question, reponse = f"CARTES/CARTES {color}/question_{nb}.png", f"CARTES/CARTES {color}/reponse_{nb}.png"
    return (question, reponse)