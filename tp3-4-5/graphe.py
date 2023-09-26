class Graphe():
    matrice_adjacence = {}
    def __init__(self, matrice_adjacence=None):
        # si la matrice d'adjacence n'est pas donnée
        # on initialise le graphe sans aucun noeud
        
        # TODO
        if matrice_adjacence is None:
            self.matrice_adjacence = {}
        else:
            for i in range(len(matrice_adjacence)):
                self.matrice_adjacence[i] = []
                for j in range(len(matrice_adjacence[i])):
                    if matrice_adjacence[i][j] == 1:
                        self.matrice_adjacence[i].append(j)
            
    
    def __str__(self):
        return (self.matrice_adjacence.__str__() + "\n")
        

    def ajouter_noeud(self,u):
    # doit ajouter u  au graphe si celui-ci n'existe pas
    # ne fait rien si il existe déjà
        # ajouter une ligne et une colonne à la matrice d'adjacence
        if self.matrice_adjacence.get(u) is None:
            self.matrice_adjacence[u] = []

    def noeuds(self):
    # renvoie la liste des noeuds
        toret = []
        for key in self.matrice_adjacence:
            toret.append(key)
        return toret

    def ajouter_arete(self,u,v):
    # ajoute l'arête de u à v
    # on suppose que u et v existent
        self.matrice_adjacence[u].append(v)


    def enlever_arete(self,u,v):
    # enlève l'arête de u à v
    # ne fait rien si elle n'existe pas
        if v in self.matrice_adjacence[u]:
            self.matrice_adjacence[u].remove(v)

    def enlever_noeud(self,u):
    # enlève le noeud u, pour garder la consistence,
    # enlève toutes les arêtes de et vers u
        for k, v in self.matrice_adjacence.items():
            if u in v:
                v.remove(u)
        self.matrice_adjacence.pop(u)



    def voisins(self,u):
    # renvoie les voisins de u (ou un itérateur sur ceux-ci)
        return self.matrice_adjacence[u]

    def nb_sommets(self):
    # renvoie le nombre de sommets
        return len(self.matrice_adjacence)  

    def nb_aretes(self):
    # renvoie le nombre d'arêtes
        nb = 0
        for key in self.matrice_adjacence:
            nb += len(self.matrice_adjacence[key])
        return nb

    def export_matrice(self):
    # renvoie une matrice d'adjacence pour
    # le graphe et un dictionnaire qui associe les
    # noms/identifiants aux indices correspondants 
    # de la matrice
        matrice = []
        dico = {}
        i = 0
        for key in self.matrice_adjacence:
            dico[key] = i
            i += 1
        for key in self.matrice_adjacence:
            matrice.append([])
            for j in range(i):
                if j in self.matrice_adjacence[key]:
                    matrice[dico[key]].append(1)
                else:
                    matrice[dico[key]].append(0)
        return matrice, dico
    



if __name__=="__main__":
# On peut écrire des tests ici, ceux-ci seront executés
# si on appelle ce fichier directement avec python graphe.py
# mais ne le seront pas lors d'un import 
    


    
    G = Graphe()
    G.ajouter_noeud(0)
    G.ajouter_noeud(1)
    G.ajouter_noeud(2)
    G.ajouter_arete(0,1)
    G.ajouter_arete(0,2)
    G.ajouter_arete(2,0)
    
    print(G)

    print("noeuds" + str(G.noeuds()))
    print("Nb sommets : " + str(G.nb_sommets()))
    print("Nb aretes : " + str(G.nb_aretes()))
    print("Voisin de 0 : " + str(G.voisins(0)))
