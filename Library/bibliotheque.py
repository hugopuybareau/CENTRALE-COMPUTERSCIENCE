#Classe Bibliotheque


from lecteur import *
from livre import *
from emprunt import *
from bibliothecaire import *
from conservateur import *
        

class Bibliotheque:
    def __init__(self,nom,c):
        self.__nom = nom
        self.__conservateur = c
        self.__lecteurs = []
        self.__livres = []
        self.__emprunts = []
        self.__bibliothecaires = []
        
    def get_nom(self):
        return self.__nom
        
    def ajouter_lecteur(self,nom,prenom,adresse,num):
        self.__lecteurs.append(Lecteur(nom,prenom,adresse,num))
    
    def get_conservateur(self):
        return self.__conservateur

    def retirer_lecteur(self,num):
        lecteur = self.chercher_lecteur_num(num)# On cherche le lecteur
        if lecteur == None:
            return False
        for e in self.__emprunts:# On verifie qu'il n'a pas d'emprunt
            if e.get_num_lecteur()==num:
                return False
        self.__lecteurs.remove(lecteur)
        return True 

    def ajouter_bibliothecaire(self,nom,prenom,adresse,num):
        if self.chercher_bibliothecaire_num(num)==None:
            self.__bibliothecaires.append(Bibliothecaire(nom,prenom,adresse,num))
        else:
            print('Ajout impossible, numéro déjà pris')
            return None
        
    def chercher_bibliothecaire_nom(self,nom):
        for l in self.__bibliothecaires:
            if l.get_nom() == nom:
                return l
        return None
    
    def supprimer_bibliothecaire(self,nom,prenom,adresse,num):
        bibliothecaire = self.chercher_bibliothecaire_nom(nom)# On cherche le bibliothecaire
        if bibliothecaire == None:
            return False
        self.__bibliothecaires.remove(bibliothecaire)# On peut ici retirer le bibliothecaire de la liste
        return True        
                      
                
    def ajouter_livre(self,auteur,titre,num,nb_tot):
        self.__livres.append(Livre(auteur,titre,num,nb_tot))
    
    def retirer_livre(self,num):
        livre = self.chercher_livre_num(num)# On cherche le livre
        if livre == None:
            return False
        for e in self.__emprunts:# On verifie que le livre n'est pas en cours d'emprunt
            if e.get_num_livre()==num:
                return False
        self.__livres.remove(livre)# On peut ici retirer le livre de la liste
        return True        
        
    def chercher_lecteur_num(self,num):
        for l in self.__lecteurs:
            if l.get_num() == num:
                return l
        return None

    def chercher_lecteur_nom(self,nom,prenom):
        for l in self.__lecteurs:
            if l.get_nom() == nom and l.get_prenom() == prenom:
                return l
        return None    
        
    def chercher_livre_num(self,num):
        for l in self.__livres:
            if l.get_num() == num:
                return l
        return None

    def chercher_livre_titre(self,titre):
        for l in self.__livres:
            if l.get_titre() == titre:
                return l
        return None    
        
    def chercher_emprunt(self, num_lecteur, num_livre, num_bibliothecaire):
        for e in self.__emprunts:
            if e.get_num_lecteur() == num_lecteur and e.get_num_livre() == num_livre and e.get_num_bibliothecaire()==num_bibliothecaire:
                return e
        return None
    

    def emprunt_livre(self, num_lecteur, num_livre, num_bibliothecaire):
        livre = self.chercher_livre_num(num_livre)# On verifie que le num de livre est valide
        if livre == None:
            print('Emprunt impossible : livre inexistant')
            return None
        if livre.get_nb_dispo() == 0:# On verifie qu'il reste des exemplaires disponibles pour ce livre
            print('Emprunt impossible : plus d\'exemplaires disponibles')
            return None
        lecteur = self.chercher_lecteur_num(num_lecteur)# On verifie que le num de lecteur est valide
        if lecteur == None:
            print('Emprunt impossible : lecteur inexistant')
            return None
        bibliothecaire=self.chercher_bibliothecaire_num(num_bibliothecaire)#On vérifie que le num du bibliothécaire est valide
        if bibliothecaire==None:
            print('Emprunt impossible : bibliothecaire inexistant')
        e = self.chercher_emprunt(num_lecteur, num_livre, num_bibliothecaire)# On verifie que ce lecteur n'a pas deja emprunte ce livre
        if e != None:
            print('Emprunt impossible : deja en cours')
            return None
        self.__emprunts.append(Emprunt(num_lecteur, num_livre, num_bibliothecaire))# Les conditions sont reunies pour pouvoir faire cet emprunt  
        livre.set_nb_dispo(livre.get_nb_dispo()-1)
        lecteur.set_nb_emprunts(lecteur.get_nb_emprunts()+1)
        return self.__emprunts[-1]


    def retour_livre(self, num_lecteur, num_livre):
        e = self.chercher_emprunt(num_lecteur, num_livre)# On recherche l'emprunt identifie par le num de livre et de lecteur
        if e != None: # l'emprunt existe, on le retire de la liste et on met a jour nb_emprunt pour le lecteur et nb_dispo pour le livre
            self.__emprunts.remove(e)
            lecteur = self.chercher_lecteur_num(num_lecteur)
            if lecteur != None : lecteur.set_nb_emprunts(lecteur.get_nb_emprunts()-1)
            livre = self.chercher_livre_num(num_livre)
            if livre != None: livre.set_nb_dispo(livre.get_nb_dispo()+1)
            print('Retour effectue')
            return True
        else:
            print('Aucun emprunt ne correspond a ces informations')
            return False
        
    def afficher_lecteurs(self):
        for l in self.__lecteurs:
            print(l)

    def afficher_livres(self):
        for l in self.__livres:
            print(l)           
            
    def afficher_emprunts(self):
        for e in self.__emprunts:
            print(e)     

    def afficher_bibliothecaires(self):
        for b in self.__bibliothecaires:
            print(b)     
           
