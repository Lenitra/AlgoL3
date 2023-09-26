from graphe import Graphe
from union_find import UnionFind
import random

class Labyrinthe:
    def __init__(self,largeur,hauteur,bouclitude=None):
        self.graphe = Graphe()
        # Pour la question 5.
        uf = UnionFind()
        # Questions 4 et 5 :
        # modifier le code ci-dessous
        self.graphe.ajouter_noeud((0,0))

    def __str__(self):
    # Génère une chaine de caractères à partir de
    # l'objet : si laby est un objet labyrinthe
    # str(laby) fait en réalité laby.__str__()
    # et implicitement print(laby) affiche cette
    # chaîne
        pass

    
