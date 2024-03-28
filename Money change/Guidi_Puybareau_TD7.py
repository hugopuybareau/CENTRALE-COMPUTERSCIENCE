import numpy as np
from math import inf

#S=[1,2,5,10,20,50,100,200,500,1000,2000,5000,10000]
#D=[10,10,10,10,1,10,10,10,10,10,10,10,10]
#P=[2.30,3.06,3.92,4.10,5.74,7.80,7.50,8.50,0.6,0.7,0.8,0.9,1]


def Monnaie31(S,M):
    mat=np.zeros([len(S)+1,M+1]) #Matrice de zéros de la taille demandée
    #print(mat)
    for i in range (len(S)+1):
        for m in range(M+1):     #Parcours de la matrice 
            if m==0:
                mat[i][m]=0      #Première colonne de 0
            elif i==0:
                mat[i][m]=inf    #Première ligne de inf sauf indice 0.0
            else :
                mat[i][m]=min(1+mat[i][m-S[i-1]] if m-S[i-1]>=0 else inf,mat[i-1][m] if i>=1 else inf) #remplissage du reste de la matrice avec la formule du TD
    return mat[len(S)][M] #Je fais le choix de renvoyer le nombre de pièce minimal au lieu de ce qui est précisé dans la méthode à cause de la question 3.1 


def Monnaie32(S,M):
    n=len(S)
    mat=[[(0,[0]*n) for j in range (M+1)] for i in range (n+1)]    #On crée la matrice à partir de la longueur de S
    #print(mat) 
    for i in range (len(S)+1):
        for m in range(M+1):
            if i==0:
                mat[i][m]=inf,[0]*n                      #Pour le cas ou il n'y a aucune pièce
            elif m==0:
                mat[i][m]=0,[0]*n                        #Pour le cas ou il n'y a rien à rembourser
            else:
                if m-S[i-1]>=0 :                         #la pièce S[i-1] est utilisée + 1 fois et le nombre de pièces utilisées prend +1 aussi quand on ajoute S[i-1] au montant de remboursement m-S[i-1]
                    nb_piece,T=mat[i][m-S[i-1]]          #T prend le détail des pièces     
                    T1=T.copy()
                    T1[i-1]+=1
                    a=nb_piece+1
                else : 
                    a,T1=inf,[0]*n
                if i>=1:                                #T2 et nb_piece ne varient pas si on rembourse m en prennant des pièces placées avant i-1 dans S 
                    nb_piece,T=mat[i-1][m]              
                    T2=T.copy()                        
                    b=nb_piece
                else:
                    b,T2=inf,[0]*n
                if a<=b:                                #Choix de la méthode qui prend le moins de pièces
                    mat[i][m]=a,T1                    
                else:
                    mat[i][m]=b,T2
    return mat[n][M]     #Si on test avec [1,3,4] pour 7€ on obtient bien 2,[0,1,1] soit 2 pièces dont une de 3 et une de 4 donc ça marche

def limite33(S,D,M):
    n=len(S)
    mat=[[(0,[0]*n) for j in range (M+1)] for i in range (n+1)]   #On crée la matrice à partir de la longueur de S
    for i in range (len(S)+1):
        for m in range(M+1):
            if i==0:
                mat[i][m]=inf,[0]*n                         #Pour le cas ou il n'y a aucune pièce
            elif m==0:
                mat[i][m]=0,[0]*n                           #Pour le cas ou il n'y a rien à rembourser
            else:
                k=0
                piece_restante=D[i-1]
                minimum,T=inf,[0]*n                            
                while k<=piece_restante and m-k*S[i-1]>=0:           #Il faut trouver quand est ce que l'on trouve le plus petit nombre de pièce en retirant S[i-1] un certain nombre de fois.
                    a,T1=mat[i-1][m-k*S[i-1]]               
                    a+=k
                    if a<minimum :                             #Choix de la méthode qui prend le moins de pièces 
                        minimum=a                             
                        T=T1.copy()
                        T[i-1]=k
                    k+=1
                mat[i][m]=minimum,T
    return mat[n][M] #ok avec limite33([1,3,4],[3,1,1],7)


def minimiser_poids35(S,P,M):
    n=len(S)
    mat=[[(0,[0]*n) for j in range (M+1)] for i in range (n+1)]  #On crée la matrice à partir de la longueur de S
    for i in range (len(S)+1):
        for m in range(M+1):
            if i==0:                                    #Pour le cas ou il n'y a aucune pièce
                mat[i][m]=inf,[0]*n
            elif m==0:
                mat[i][m]=0,[0]*n                       #Pour le cas ou il n'y a rien à rembourser
            else:
                if m-S[i-1]>=0:                         #Le nombre d'utilisation de S[i-1] prend +1, le poids prend sa valeur + celle de S[i-1] dès que l'on ajoute S[i-1] à ce qui a été utilisé pour rembourser m-S[i-1]
                    poids,T=mat[i][m-S[i-1]]             
                    T1=T.copy()                         
                    T1[i-1]+=1
                    a=poids+P[i-1]
                else : 
                    a,T1=inf,[0]*n
                if i>=1:                                #T2 et poids ne varient pas si on rembourse m en prennant des pièces placées avant i-1 dans S
                    poids,T=mat[i-1][m]                    
                    T2=T.copy()                         
                    b=poids
                else:
                    b,T2=inf,[0]*n
                if a<=b:                                #Choix de la méthode qui "pèse le moins lourd"
                    mat[i][m]=a,T1                      
                else:
                    mat[i][m]=b,T2
    return mat[n][M]
    

S=[1,3,4,7]
P=[10,27,32,55]

def Poids_Gloutonne36(S,P,M):
    L=[(P[i]/S[i],S[i],P[i]) for i in range (len(P))]
    L.sort()
    Mprime=M
    res=0
    while Mprime !=0:
        k=0
        while L[k][1]>Mprime:
            k=k+1
        s=L[k][1]
        p=L[k][2]
        res=res+p*(Mprime//s)
        Mprime=Mprime%s
    return res 
    
L, K, J= [], [], []
for i in range (1,21) :
    L.append(Poids_Gloutonne36(S, P, i))
    K.append(minimiser_poids35(S, P, i)[0])
    J.append(i)
print(L)
print(K)
print(J)
        
             
    
                    
                    
                    
                    
                
                
            
            
                
            