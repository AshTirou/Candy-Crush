print("SIUUUUUUUU")
def genere_grille(taille : int, nb_bonbons : int) -> list :
    """Genere une grille en 2D de taille donnée avec un nombre de bonbons différents donnés


    Args:
        taille (int): Taille de la grille du Jeu
        nb_bonbons (int): Nombre de bonbons différents dans le jeu

    Returns:
        list: Renvoie un tableau 2D
    """

def inverse_case(grille : list, coord_1 : tuple, coord_2 : tuple ) -> list :
    """Inverse les bonbons des deux cases si possible 

    Args:
        grille (list): Grille du Jeu
        coord_1 (tuple): Coordonnées (i,j) d'un bonbon
        coord_2 (tuple): Coordonnées (i,j) d'un bonbon

    Returns:
        list: Renvoie la grille du jeu modifiée
    """

def analyse_combinaison(grille_modified:list, niveau:int) -> bool : 
    """Vérifier si la combinaison est complète en fonction du niveau.

    Args:
        niveau (int): valeur du niveau
        grille_modified (list): Nouvelle grille avec l'inversement

    Returns:
        bool: renvois True si l'inversement fonctionne sinon renvois False.
    """

def complete_emplacements_vides(grille:list, index_combinaison_deleted:tuple) -> list:
    """Permet que'après combinaison suprimée, déplacer ligne ou colonne, puis completer avec couleur aléatoire les cases vides.

    Args:
        grille (list): Grille du Jeu
        index_combinaison_deleted (tuple): Coordonnées (i,j) d'une combinaison.

    Returns:
        list: Renvois la grille modifié
    """

def partie_fini(grille:list) -> bool:
    """Renvois si oui ou non, la partie est terminée.

    Args:
        grille (list): Grille du jeu.

    Returns:
        bool: renvois True si parti fini, sinon renvois false.
    """