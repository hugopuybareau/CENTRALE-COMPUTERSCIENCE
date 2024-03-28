#Class Consevateur


from personne import *
from bibliothecaire import *

class Conservateur(Personne) :
    
    def __init__(self,nom,prenom,adresse,bib):
        Personne.__init__(self,nom,prenom,adresse)
        self.__bibliothecaire=[]
        self.__bibliotheque=bib
    
    def get_bibliotheque(self):
        return self.__bibliotheque
    
    def __str__(self):
        pr=Personne.get_prenom(self)
        nom=Personne.get_nom(self)
        ad=Personne.get_adresse(self)
        return f"Classe Conservateur - Nom : {nom}, Prenom : {pr}, Adresse : {ad}, Bibliotheque : {self.__bibliotheque}"
    


        
    
        