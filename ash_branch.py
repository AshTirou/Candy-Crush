from random import randint
import matplotlib.pyplot as plt



def affichage_grille(grille, nb_type_bonbons):
    """
    Affiche la grille de jeu "grille" contenant au
    maximum "nb_type_bonbons" couledetecte_coordonnees_combinaisonurs de bonbons différentes.
    """
    plt.imshow(grille, vmin=0, vmax=nb_type_bonbons-1, cmap='jet')
    """
    long = len(grille)
    for i in range(long):
      y""" 
    plt.yticks(np.arange(0,len(grille)-1,1))
    plt.xticks(np.arange(0,len(grille)-1,1))
    plt.pause(0.1)
    plt.draw()
    plt.pause(0.1)



grille = [
    [  3  , 1 , 3 , 1],
    
    [2 , 3 , 1 , 1],
    
    [2 , 1 , 3 , 2],
    
    [0 , 0 , 0 , 1]     
    
    ]

index_empty = [(3,0),(3,1),(3,2)]
affichage_grille(grille, 4)
grille = complete_emplacements_vides(grille,index_empty,3)
    
affichage_grille(grille, 4)
