import pygame
import numpy as np
from Point import *
import copy
from Timer import *
from Tetramino import *
from interface import *
import random
class Plateau:
    def __init__(self, interface):
        self.interface = interface
        self.largeur = interface.ecran.get_width() // interface.taille_fonte_x
        self.hauteur = interface.ecran.get_height() // interface.taille_fonte_y
        self.grille = np.zeros((self.hauteur-2, self.largeur-2), dtype=int)
        self.tetraminos = []
        self.score = 0
        self.index = 0
        self.nombre_lignes=0

    def dessiner(self):
        self.interface.ecran.fill(self.interface.COULEUR['noir'])
        s=str(self.score)
        for i in range(len(s)):
            self.interface.cursor = (i, 0)
            self.interface.write(s[i],fgcolor=self.interface.COULEUR['vert'])
        for i in range(len(s),12):
            self.interface.cursor = (i, 0)
            self.interface.write("#",fgcolor=self.interface.COULEUR['rouge'])

        for x in range(12):

            self.interface.cursor = (x, 21)
            self.interface.write("#",fgcolor=self.interface.COULEUR['rouge'])
        for x in range(1,22):
            self.interface.cursor = (0, x)
            self.interface.write("#",fgcolor=self.interface.COULEUR['rouge'])
            self.interface.cursor = (11, x)
            self.interface.write("#",fgcolor=self.interface.COULEUR['rouge'])
        for y in range(self.hauteur-2):
            for x in range(self.largeur-2):
                if self.grille[y, x] != 0:
                    couleur = self.interface.COULEUR['blanc']
                    self.interface.curseur(x+1,y+1)
                    self.interface.write("X",fgcolor=self.interface.COULEUR['blanc'],bgcolor=self.interface.COULEUR['noir'])
        for tetramino in self.tetraminos:
            for point in tetramino.image():
                x, y = point.to_tuple()
                if 0 <= x < self.largeur-2 and 0 <= y < self.hauteur-2:
                    self.interface.curseur(x+1,y+1)
                    self.interface.write("X",fgcolor=self.interface.COULEUR['noir'],bgcolor=tetramino.couleur())
        self.interface.mise_a_jour()

    def ajouter_tetramino(self, tetramino):
        self.tetraminos.append(tetramino)

    def peut_bouger(self, tetramino, deplacement):
        for point in tetramino.image():
            nouvelle_position = point + deplacement
            x, y = nouvelle_position.to_tuple()
            if not (0 <= x < self.largeur-2 and 0 <= y < self.hauteur-2):
                return False
            if self.grille[y, x] != 0:
                return False
        return True

    def poser_tetramino(self, tetramino):
        for point in tetramino.image():
            x, y = point.to_tuple()
            if 0 <= x < self.largeur-2 and 0 <= y < self.hauteur-2:
                self.grille[y, x] = 1
        self.tetraminos.remove(tetramino)
        self.supprimer_lignes_completes()

    def supprimer_lignes_completes(self):
        lignes_a_supprimer = [i for i in range(self.hauteur-2) if all(self.grille[i, :])]
        for ligne in lignes_a_supprimer:
            self.grille = np.delete(self.grille, ligne, 0)
            self.grille = np.vstack([[0] * (self.largeur-2), self.grille])
        nombre_lignes = len(lignes_a_supprimer)
        if nombre_lignes == 1:
            self.score += 40
        elif nombre_lignes == 2:
            self.score += 100
        elif nombre_lignes == 3:
            self.score += 300
        elif nombre_lignes == 4:
            self.score += 1200
        self.nombre_lignes = nombre_lignes


    def verifier_collision(self, tetramino):
        for point in tetramino.image():
            x, y = point.to_tuple()
            if y >= self.hauteur-2 or (0 <= y < self.hauteur-2 and 0 <= x < self.largeur-2 and self.grille[y, x] != 0):
                return True
        return False

    def game_over(self):
        for x in range(self.largeur-2):
            if self.grille[0, x] != 0:
                return True
        return False




