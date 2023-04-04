from random import randint
import matplotlib.pyplot as plt


def analyse_combinaison(grille_modified: list) -> bool:
  """Vérifie si une combinaison existe dans la grille (au moins 3 bonbons identiques alignés.
  Lucas
    
  Args:
      grille_modified (list): Nouvelle grille avec l'inversement

  Returns:
      bool: renvoie True si l'inversement fonctionne sinon renvois False.
  """



def affichage_grille(grille, nb_type_bonbons):
  """
    Affiche la grille de jeu "grille" contenant au
    maximum "nb_type_bonbons" couleurs de bonbons différentes.
    """
  plt.imshow(grille, vmin=0, vmax=nb_type_bonbons - 1, cmap='jet')
  plt.pause(0.1)
  plt.draw()
  plt.pause(0.1)


grille = [[0, 2, 0, 0, 2], [2, 1, 0, 2, 2], [1, 2, 1, 0, 1], [0, 2, 0, 1, 2],
          [2, 0, 1, 0, 2]]


def etat(grille, i, j):
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

  return bonbon_a_suprimer_finale


affichage_grille(grille, 4)
