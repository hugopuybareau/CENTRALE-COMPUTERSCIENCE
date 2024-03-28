#Classe Lecteur


from personne import *

       
class Lecteur(Personne):
    def __init__(self,nom,prenom,adresse,num):
        Personne.__init__(self,nom,prenom,adresse)        
        self.__num = num
        self.__nb_emprunts = 0
        
    def set_num(self,num):
        self.__num = num
        
    def get_num(self):
        return self.__num
        
    def set_nb_emprunts(self,nb_emprunts):
        self.__nb_emprunts = nb_emprunts
        
    def get_nb_emprunts(self):
        return self.__nb_emprunts
        
    def __str__(self): #Affichr les proprietes de l'objet grâce à la fonction print
        return 'Lecteur - Nom : {}, Prenom : {}, Adresse : {}, Numero : {}, Nb emprunts : {}'.format(self.get_nom(),self.get_prenom(),self.get_adresse(),self.__num)
