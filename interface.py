import pygame
from pygame.locals import*
import random
import numpy as np
import time
class KST:
    __slots__ = ()  # empêche la ré-écriture accidentelle des constantes  

    # codes numériques pour les 4 directions, utilisés aussi par le module
    # d'inteface graphique
    HAUT = 0
    DROITE = 1
    BAS = 2
    GAUCHE = 3
    ESPACE = 4


class Interface:
    def __init__(self, dim_x, dim_y, titre):
        self.last_key_time = time.time()
        self.clock = pygame.time.Clock()
        self.cursor = (0, 0)
        self.taille_fonte_y = 30
        pygame.init()
        if not pygame.font.get_init():
            print("Désolé, les fontes de caractères sont absentes, je ne peux démarrer")
            quit()
        self.font = pygame.font.SysFont("Courrier, Monospace",self.taille_fonte_y)
        self.taille_fonte_x = self.font.size('M')[0]
        self.ecran = pygame.display.set_mode((dim_x * self.taille_fonte_x ,
                                          dim_y * self.taille_fonte_y))
        pygame.display.set_caption(titre)
        self.COULEUR = {  # un dictionnaire: comme une liste mais indexé par des chaînes ici
            'vert'   : (11, 240, 11),    # "vert" défini par intensités (rouge, vert, bleu)
            'rouge'   : (213, 11, 11),
            'orange'   : (213, 180, 11),
            'jaune'   : (213, 213, 11),
            'bleu'    : (40, 40, 240),
            'blanc'   : (255, 255, 255),
            'gris'   : (210, 210, 210),
            'noir'    : (0, 0, 0)
        }
        self.NOM_COULEUR = list(self.COULEUR.keys())

    # place le "curseur" : la position de la prochaine commande "write"
    def curseur(self, x, y):
        self.cursor = (x, y)
        
    # écrire une chaine à la position du curseur
    def write(self, texte, fgcolor=(255,255,255), bgcolor=(0,0,0)):
        texte = self.font.render(texte,
                            True,
                            pygame.Color(fgcolor),
                            pygame.Color(bgcolor))
        self.ecran.blit(texte,
                        (self.cursor[0]*self.taille_fonte_x,
                         self.cursor[1]*self.taille_fonte_y))

    # faire une temporisation
    def pause(self, tempo): 
        self.clock.tick(tempo)

    # affiche les modifications effectuées depuis le dernier appel
    def mise_a_jour(self):
        pygame.display.flip()

    # retourne code d'une touche de déplacement du clavier (touches "flêches")
    # ou None sinon
    def lire_touche(self):
        key = None
        current_time = time.time()
        time_elapsed = current_time - self.last_key_time
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.fermer()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    key = KST.HAUT
                elif event.key == pygame.K_DOWN:
                    key = KST.BAS
                elif event.key == pygame.K_LEFT:
                    key = KST.GAUCHE
                elif event.key == pygame.K_RIGHT:
                    key = KST.DROITE
                elif event.key == pygame.K_SPACE:  # Ajoutez cette ligne pour détecter la touche espace
                    key = KST.ESPACE

        if key is not None:
            self.last_key_time = current_time
            return key

        if time_elapsed > 0.15:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                self.last_key_time = current_time
                return KST.DROITE
            if keys[pygame.K_LEFT]:
                self.last_key_time = current_time
                return KST.GAUCHE
            if keys[pygame.K_UP]:
                self.last_key_time = current_time
                return KST.HAUT
            if keys[pygame.K_DOWN]:
                self.last_key_time = current_time
                return KST.BAS
            if keys[pygame.K_SPACE]:  # Ajoutez cette ligne pour tester l'appui continué de la touche espace
                self.last_key_time = current_time
                return KST.ESPACE
        return None

    # ferme la librairie (au cas où la fenêtre graphique reste "bloquée"
    def fermer(self):
        pygame.quit()

