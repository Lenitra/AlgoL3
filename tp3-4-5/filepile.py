class Element:
    precedent = None
    prochain = None
    contenu = None
    # Un élément de la liste chaînée
    def __init__(self, precedent, prochain, contenu):
        self.precedent = precedent
        self.prochain = prochain    
        self.contenu = contenu


class FilePile:
    # Une file/pile implémentée avec une liste chaînée
    start = None
    end = None



    def __init__(self):
    # Une file/pile sera toujours vide à l'initialisation
        self.start = None
        self.end = None

        
    def pop(self):
        # récupère le premier élément de la liste chaînée
        # en l'enlevant de celle-ci
        if self:
            tmp = self.start
            self.start = tmp.prochain
            return tmp.contenu
        else:
            return None



    def pushFirst(self,contenu):
        if self:
            tmp = Element(None,None,contenu)
            tmp.prochain = self.start
            self.start.precedent = tmp
            self.start = tmp
        else:
            tmp = Element(None,None,contenu)
            self.start = tmp
            self.end = tmp
        
        

    def pushLast(self,contenu):
        #insère à la fin de la liste chaînée
        if self:
            tmp = Element(None,None,contenu)
            tmp.precedent = self.end
            self.end.prochain = tmp
            self.end = tmp
        else:
            tmp = Element(None,None,contenu)
            self.start = tmp
            self.end = tmp
        
        

    def __bool__(self): 
        # doit renvoyer True si la liste contient au moins un élément
        # et false sinon : permet de faire if FilePile:
        if self.start is None:
            return False
        else:
            return True
        
    
        

    def __iter__(self):
        # (bonus) On pourra définir un itérateur sur notre liste
        # pour pouvoir faire for x in file:
        tmp = self.start
        while tmp is not None:
            yield tmp.contenu
            tmp = tmp.prochain


    def __str__(self):
        # (bonus) On pourra afficher la liste
        # avec print
        toret = ""
        tmp = self.start
        while tmp is not None:
            toret += str(tmp.contenu) + " "
            tmp = tmp.prochain
        return toret
    
        

if __name__=="__main__":
    # créer une FilePile
    fp = FilePile()
    print("Création d'une FilePile vide")
    print(str(fp))
    print("Ajout de 1, 2, 3 au début")
    fp.pushFirst(3)
    fp.pushFirst(2)
    fp.pushFirst(1)
    print(str(fp))
    print("Ajout de 4, 5, 6 à la fin")
    fp.pushLast(4)
    fp.pushLast(5)
    fp.pushLast(6)
    print(str(fp))
    