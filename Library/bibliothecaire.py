#Class Bibliothécaire


from personne import *

class Bibliothecaire(Personne):
    def __init__(self,nom,prenom,adresse,num):
        Personne.__init__(self,nom,prenom,adresse)
        self.__num=num
        
    def set_num(self,num):
        self.__num = num
            
    def get_num(self):
        return self.__num
        
    def __str__(self):
        return 'Bibliothecaire - Nom : {}, Prenom : {}, Adresse : {}, Numero : {}'.format(self.get_nom(),self.get_prenom(),self.get_adresse(),self.__num)
