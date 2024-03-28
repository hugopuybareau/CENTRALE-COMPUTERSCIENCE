#Classe Livre 

       
class Livre:
    def __init__(self,titre,auteur,num,nb_tot):
        self.__titre = titre        
        self.__auteur = auteur
        self.__num = num
        self.__nb_tot = nb_tot
        self.__nb_dispo = nb_tot

    def set_auteur(self,auteur):
        self.__auteur = auteur
        
    def get_auteur(self):
        return self.__auteur
        
    def set_titre(self,titre):
        self.__titre = titre
        
    def get_titre(self):
        return self.__titre
        
    def set_num(self,num):
        self.__num = num
        
    def get_num(self):
        return self.__num
    
    def set_nb_tot(self,nb_tot):
        self.__nb_tot = nb_tot
        
    def get_nb_tot(self):
        return self.__nb_tot

    def set_nb_dispo(self,nb_dispo):
        self.__nb_dispo = nb_dispo
        
    def get_nb_dispo(self):
        return self.__nb_dispo
        
    def __str__(self):
        return 'Livre - Auteur : {}, Titre : {}, Numero : {}, Nb tot : {}, Nb dispo : {}'.format(self.__auteur,self.__titre,self.__num,self.__nb_tot,self.__nb_dispo)
