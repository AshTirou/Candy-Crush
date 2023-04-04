'''IMPORTATION DES MODULES'''
from random import randint
from copy import *
import matplotlib.pyplot as plt
import numpy as np
# ATTENTION I = LIGNE et J = COLONNE
''' FONCTIONS '''


def genere_grille(taille: int, nb_bonbons: int) -> list:
  """Genere une grille en 2D de taille donnée avec un nombre de bonbons différents donnés ~ Baptiste
    Args:
        taille (int): Taille de la grille du Jeu
        nb_bonbons (int): Nombre de bonbons différents dans le jeu

    Returns:
        list: Renvoie un tableau 2D
    """
  grille = []
  for i in range(taille):
    liste = []
    for j in range(taille):
      liste.append(randint(1, nb_bonbons))
    grille.append(liste)
  return grille


def echangeable(taille_grille, i, j):
  if i < 0:
    return False
  elif i > taille_grille - 1:
    return False
  elif j < 0:
    return False
  elif j > taille_grille - 1:
    return False
  else:
    return True


def analyse_jeu_fini(grille: list[list]) -> bool:
  taille_grille = len(grille)
  stop = False
  i = 0
  j = 0
  while i < taille_grille and stop != True:
    while j < taille_grille and stop != True:
      if echangeable(taille_grille, i - 1, j):
        new_liste = inverse_case(grille, (i, j), (i - 1, j))
        if len(detecte_coordonnees_combinaison(new_liste, i - 1, j)) > 1:
          stop = True
      if echangeable(taille_grille, i + 1, j):
        new_liste = inverse_case(grille, (i, j), (i + 1, j))
        if len(detecte_coordonnees_combinaison(new_liste, i + 1, j)) > 1:
          stop = True
      if echangeable(taille_grille, i, j - 1):
        new_liste = inverse_case(grille, (i, j), (i, j - 1))
        if len(detecte_coordonnees_combinaison(new_liste, i, j - 1)) > 1:
          stop = True
      if echangeable(taille_grille, i, j + 1):
        new_liste = inverse_case(grille, (i, j), (i, j + 1))
        if len(detecte_coordonnees_combinaison(new_liste, i, j + 1)) > 1:
          stop = True
      j += 1
    j = 0
    i += 1
  return stop


def affichage_grille(grille, nb_type_bonbons):
  """
    Affiche la grille de jeu "grille" contenant au
    maximum "nb_type_bonbons" couledetecte_coordonnees_combinaisonurs de bonbons différentes.
    """
  plt.imshow(grille, vmin=0, vmax=nb_type_bonbons, cmap='jet')
  plt.yticks(np.arange(0, len(grille), 1))
  plt.xticks(np.arange(0, len(grille), 1))
  plt.pause(0.1)
  plt.draw()
  plt.pause(0.1)


def inverse_case(grille: list, coord_1: tuple, coord_2: tuple) -> list:
  """Inverse les bonbons des deux cases si possible (si au moins un des deux crée une combinaison) ~ Paul

    Args:
        grille (list): Grille du Jeu
        coord_1 (tuple): Coordonnées (i,j) d'un bonbon
        coord_2 (tuple): Coordonnées (i,j) d'un bonbon

    Returns:
        list: Renvoie la grille du jeu modifiée
    """
  grille_copy = deepcopy(grille)
  if abs(coord_1[0] - coord_2[0]) + abs(coord_1[1] - coord_2[1]) != 1:
    print("Veuillez sélectioner deux cases adjacentes")
  elif coord_1[0] < 0 or coord_1[0] >= len(
      grille) or coord_1[1] < 0 or coord_1[1] >= len(
        grille[0]) or coord_2[0] < 0 or coord_2[0] >= len(
          grille) or coord_2[1] < 0 or coord_2[1] >= len(grille[0]):
    print("Veuillez sélectioner des coordonnées qui existent")
  else:
    grille_copy[coord_1[0]][coord_1[1]], grille_copy[coord_2[0]][
      coord_2[1]] = grille_copy[coord_2[0]][coord_2[1]], grille_copy[
        coord_1[0]][coord_1[1]]
  return grille_copy


def analyse_combinaison(grille: list) -> bool:
  """Vérifie si une combinaison existe dans la grille (au moins 3 bonbons identiques alignés. ~ Lucas
    
    Args:
        grille (list): Nouvelle grille avec l'inversement

    Returns:
        bool: renvoie True si l'inversement fonctionne sinon renvois False.
  """
  #print("Début")
  grille_size = len(grille)
  i = 0
  combinaison_possible = False
  while i < grille_size and not combinaison_possible:
    j = 0
    while j < grille_size and not combinaison_possible:
      for coord in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:

        if i - 1 < 0 or i + 1 == grille_size or j - 1 < 0 or j + 1 == grille_size:
          combinaison = False
        else:
          grille_temp = inverse_case(grille, (i, j), coord)
          combinaison = detecte_coordonnees_combinaison(
            grille_temp, coord[0], coord[1])
        #print(combinaison, coord)
        if combinaison != False and len(combinaison) > 1:

          combinaison_possible = True
          position_finale = coord
        print(i, j)
      j += 1
    i += 1
  #print(combinaison_possible)
  #print('Fin')
  if combinaison_possible:
    return grille_temp, combinaison, (i, j), coord
  else:
    return False


def destroy_combinaisons_existantes(grille):
  """Supprime toutes les combinaisons qui existent déjà dans le jeu
  Modifie la grille du Jeu en place
  Ashwine
    
    Args:
        grille (list): Grille du Jeu

    Returns:
        None
  """
  grille_size = len(grille)
  i = 0

  while i < grille_size:
    j = 0

    while j < grille_size:
      # Vérifie s'il existe une combinaison sur la case indiquée
      combinaison = detecte_coordonnees_combinaison(grille, i, j)

      # Si une combinaison existe, alors on la supprime et on effectue de nouveau la recherche
      if combinaison != [(i, j)]:
        supprime_bonbons(grille, combinaison)
        complete_emplacements_vides(grille, combinaison, nb_bonbons)
        affichage_grille(grille, nb_bonbons)
        i, j = 0, 0

      j += 1
    i += 1


def etat(grille, i, j):
  """
  Renvois la valeur d'une case de coordonée (i,j) en évitant le dépassement de borne.
  Args :
    grille (list) : grille de jeu 
  
  Return :
    valeur case de coordonée (i,j)
  
  """
  longeur = len(grille)
  if i < 0:
    return -1
  elif i > longeur - 1:
    return -1
  elif j < 0:
    return -1
  elif j > longeur - 1:
    return -1
  else:
    return grille[i][j]


def detecte_coordonnees_combinaison(grille, i, j):
  """
  Renvoie une liste contenant les coordonnées de tous les bonbons
  appartenant à la combinaison du bonbon (i, j).
  """
  type_bonbon = grille[i][j]
  bonbon_a_suprimer_finale = []

  liste_bonbon_in_combinaison_horizontale = []
  nbr_bonbon_in_combinaison_horizontale = 0
  index = 1
  # on regarde a gauche
  while etat(grille, i, j - index) == type_bonbon:
    liste_bonbon_in_combinaison_horizontale.append((i, j - index))
    nbr_bonbon_in_combinaison_horizontale += 1
    index += 1

  # on regarde à droite
  index = 1
  while etat(grille, i, j + index) == type_bonbon:
    liste_bonbon_in_combinaison_horizontale.append((i, j + index))
    nbr_bonbon_in_combinaison_horizontale += 1
    index += 1

  if nbr_bonbon_in_combinaison_horizontale >= 2:
    bonbon_a_suprimer_finale += liste_bonbon_in_combinaison_horizontale

  liste_bonbon_in_combinaison_verticale = []
  nbr_bonbon_in_combinaison_verticale = 0

  # en bas
  index = 1
  while etat(grille, i - index, j) == type_bonbon:
    liste_bonbon_in_combinaison_verticale.append((i - index, j))
    nbr_bonbon_in_combinaison_verticale += 1
    index += 1

  # en haut
  index = 1
  while etat(grille, i + index, j) == type_bonbon:
    liste_bonbon_in_combinaison_verticale.append((i + index, j))
    nbr_bonbon_in_combinaison_verticale += 1
    index += 1

  if nbr_bonbon_in_combinaison_verticale >= 2:
    bonbon_a_suprimer_finale += liste_bonbon_in_combinaison_verticale

  return sorted(bonbon_a_suprimer_finale + [(i, j)])


def supprime_bonbons(grille: list, list_combi: list) -> list:
  """
  Supprime les élements des indices contenues dans list_combi

      Args: grille (list)
            list_combi (list) : Tableau contenant les indices des élements à supprimer
  
    Returns:
        list : Renvoie la grille modifiée
        list : Renvoie positions des bonbons supprimés sous forme de liste
  """
  for i in range(len(list_combi)):
    grille[list_combi[i][0]][list_combi[i][1]] = 0


def complete_emplacements_vides(grille: list, list_index_empty: list,
                                nb_bonbons: int) -> list:
  """
  Permet que'après combinaison suprimée, déplacer ligne ou colonne, puis completer avec couleur aléatoire les cases vides.
  Modifie la grille du Jeu en place
    Ashwine

    Args:
      grille (list): Grille du jeu
      list_index_empty (list) : Liste contenant les emplacements vides
      nb_bonbons (int): Nombre de bonbons différents dans le jeu
      

    Return:
        None
  """
  for index in list_index_empty:
    temp = index[0]
    if grille[temp][index[1]] == 0:
      while temp > 0:
        grille[temp][index[1]] = grille[temp - 1][index[1]]
        temp -= 1
      grille[temp][index[1]] = randint(1, nb_bonbons)


def request_user(size_grille) -> tuple:
  """
  Demande à l'utilisateur le bonbon qu'il souhaite déplacer et la destination de celle-ci
  Ashwine

    Args:
      None

    Returns:
        bonbon_initial_v2 (tuple) : Emplacement du Bonbon à déplacer
        bonbon_final_v2 (tuple) : Emplacement final du Bonbon
  """

  #Coordonnées du Bonbon à déplacer
  request = True

  while request:

    bonbon_init_list = input("Coordonnées du Bonbon Départ \n").split(".")
    bonbon_final_list = input("Coordonnées du Bonbon Final \n").split(".")

    try:  #Si valeur entrée valide
      bonbon_initial_v2 = (int(bonbon_init_list[0]), int(bonbon_init_list[1]))
      bonbon_final_v2 = (int(bonbon_final_list[0]), int(bonbon_final_list[1]))
      request = False
      #Si coordonnées en dehors de la grille
      if bonbon_initial_v2[0] < 0 or bonbon_initial_v2[
          0] >= size_grille or bonbon_initial_v2[1] < 0 or bonbon_initial_v2[
            1] >= size_grille or bonbon_final_v2[0] < 0 or bonbon_final_v2[
              0] >= size_grille or bonbon_final_v2[1] < 0 or bonbon_final_v2[
                1] >= size_grille:
        request = True

    except:
      print("La valeur entrée est incorrecte \n")

  print('')

  return bonbon_initial_v2, bonbon_final_v2


def partie_finie_gars(grille: list) -> bool:
  """Renvoie si oui ou non, la partie est terminée.

    Args:
        grille (list): Grille du jeu.

    Returns:
        bool: renvoie True si partie finie, sinon renvoie false.
    """


'''PROGRAMME PRINCIPAL'''

# Initialisation de la Grille du Jeu
print(
  "\t \t \t \t Candy Crush \n \n Indiquez les coordonnées sous la forme suivante : \n \t ligne.colonne \n Veuillez respecter la syntaxe ! \n Amusez vous bien ! ^^ \n"
)
taille_grille = int(input("Quelle est la taille de la grille du jeu ? \n"))
nb_bonbons = int(input("Combien de bonbons différents ? \n"))
grille = genere_grille(taille_grille, nb_bonbons)
destroy_combinaisons_existantes(grille)
affichage_grille(grille, nb_bonbons)

# Lancement du Jeu

while analyse_jeu_fini(grille):

  bonbon_init, bonbon_final = request_user(taille_grille)
  grille_temp = inverse_case(grille, bonbon_init, bonbon_final)
  combinaison_f = detecte_coordonnees_combinaison(grille_temp, bonbon_final[0],
                                                  bonbon_final[1])
  combinaison_i = detecte_coordonnees_combinaison(grille_temp, bonbon_init[0],
                                                  bonbon_init[1])

  if combinaison_i != [bonbon_init] or combinaison_f != [bonbon_final]:

    if combinaison_i != [bonbon_init]:
      combinaison = combinaison_i
    else:
      combinaison = combinaison_f

    grille = deepcopy(grille_temp)
    supprime_bonbons(grille, combinaison)
    complete_emplacements_vides(grille, combinaison, nb_bonbons)
    destroy_combinaisons_existantes(grille)
    affichage_grille(grille, nb_bonbons)
