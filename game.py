import sqlite3
from random import shuffle

list_nb = list(range(1, 61))  # Initialisation d'une liste contenant tous les numéros des questions
shuffle(list_nb)  # Mélange de la liste list_nb


def comparaison_levenshtein(mot1 : str, mot2 : str):
    """Algorithme comparant deux chaînes de caractères

    Args:
        str1 (str): mot n°1
        str2 (str): mot n°2
    Return:
        (int) : Nombre de différences entre les deux chaînes de caractères
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
    
def question():
    conn = sqlite3.connect('database.db') # Variable permettant de faire la liaison entre la BDD et le programme executé
    c = conn.cursor() # Instance de classe permettant d'exécuter dans la BDD différentes requêtes
    nb = list_nb[0] # On prend la première question dans la liste qui a été mélangé au préalable
    del(list_nb[0]) # On supprime cette question pour éviter qu'elle réapparaisse une 2e fois
    request = c.execute(f"SELECT * FROM cartes WHERE id={nb}") # Exécution de la requête SQL
    request = request.fetchall()[0] # Transformation de l'objet cursor en tuple traitable
    conn.close() # Fermeture de la base de données
    return request



