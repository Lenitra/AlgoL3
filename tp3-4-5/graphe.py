class Graphe():
    matrice_adjacence = {}
    def __init__(self, matrice_adjacence=None):
        # si la matrice d'adjacence n'est pas donnée
        # on initialise le graphe sans aucun noeud
        
        # TODO
        if matrice_adjacence:
            self.matrice_adjacence = matrice_adjacence
            
    
    def __str__(self):
        return self.matrice_adjacence
        

    def ajouter_noeud(self,u):
    # doit ajouter u  au graphe si celui-ci n'existe pas
    # ne fait rien si il existe déjà
        # ajouter une ligne et une colonne à la matrice d'adjacence
        self.matrice_adjacence.append([0]*len(self.matrice_adjacence))

    def noeuds(self):
    # renvoie la liste des noeuds
        toret = []
        for i in range(len(self.matrice_adjacence)):
            toret.append(i)
        return toret

    def ajouter_arete(self,u,v):
    # ajoute l'arête de u à v
    # on suppose que u et v existent
        pass

    def enlever_arete(self,u,v):
    # enlève l'arête de u à v
    # ne fait rien si elle n'existe pas
        pass

    def enlever_noeud(self,u):
    # enlève le noeud u, pour garder la consistence,
    # enlève toutes les arêtes de et vers u
        pass

    def voisins(self,u):
    # renvoie les voisins de u (ou un itérateur sur ceux-ci)
        pass

    def nb_sommets(self):
    # renvoie le nombre de sommets
        pass

    def nb_aretes(self):
    # renvoie le nombre d'arêtes
        pass

    def export_matrice(self):
    # renvoie une matrice d'adjacence pour
    # le graphe et un dictionnaire qui associe les
    # noms/identifiants aux indices correspondants 
    # de la matrice
        pass



if __name__=="__main__":
# On peut écrire des tests ici, ceux-ci seront executés
# si on appelle ce fichier directement avec python graphe.py
# mais ne le seront pas lors d'un import 
    

    G1 = {
            0 : {
                1 : True,
                2 : True,
                3 : True,
                },
            1 : {
                3 : True,
                },
            2 : {},
            3 : {
                0 : True,
                1 : True,
                },
        }
    
    G = Graphe(G1)

    print(G.noeuds())

