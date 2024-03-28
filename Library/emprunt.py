#Class Emprunt

from datetime import date
from lecteur import *
from livre import *
from bibliothecaire import *

     
class Emprunt:
    def __init__(self,num_lecteur,num_livre,num_bibliothecaire,date):
        self.__num_lecteur = num_lecteur
        self.__num_livre = num_livre
        self.__date = date
        self.__num_bibliothecaire=num_bibliothecaire

    def get_num_lecteur(self):
        return self.__num_lecteur
        
    def get_num_livre(self):
        return self.__num_livre
        
    def get_num_bibliothecaire(self):
        return self.__num_bibliothecaire
    
    def set_date(self,date):
        self.__date = date
        
    def get_date(self):
        return self.__date

    def __str__(self):
        return 'Emprunt - Numero lecteur : {}, Numero livre: {}, Numero Biliothecaire: {}, Date : {}'.format(self.__num_lecteur,self.__num_livre,self.__num_bibliothecaire,self.__date)