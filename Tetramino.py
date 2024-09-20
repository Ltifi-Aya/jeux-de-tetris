import copy
from Point import *
class Tetramino:
    def __init__(self, points, position=Point(0, 0), rotation=0, color=(255, 255, 255)):

        self.points = points
        self.position = position
        self.rotation = rotation
        self.color = color

    def translater(self, deplacement):

        self.position += deplacement

    def tourner(self,largeur_plateau):

        self.rotation = (self.rotation + 90) % 360
        self.ajuster_position(largeur_plateau)

    def image(self):
        """
        Retourne la liste des points/cellules après rotation et translation
        (coordonnées réelles sur le plateau de jeu).

        """
        rotated_points = [point.rotate(self.rotation) for point in self.points]
        return [self.position + point for point in rotated_points]

    def ajuster_position(self, largeur_plateau):
        """
        Ajuste la position du tétramino pour qu'il reste à l'intérieur de l'écran après la rotation.
        """
        points_apres_rotation = self.image()
        min_x = min(point.x for point in points_apres_rotation)
        max_x = max(point.x for point in points_apres_rotation)

        if min_x < 0:
            self.position.x += abs(min_x)
        elif max_x >= largeur_plateau:
            self.position.x -= (max_x - largeur_plateau + 1)
    def couleur(self):
        """
        Retourne la couleur associée à la forme du tétramino.
        """
        return self.color

    def cloner(self):
        """
        Retourne une copie du tétramino.
        """
        return copy.deepcopy(self)

#Fonction qui retourne un tetramino à partir de sa forme et position.
def create_tetramino(shape,pos):
    if shape == 'I':
        points = [Point(0, 0), Point(1, 0), Point(-1, 0), Point(-2, 0)]
        color = (0, 255, 255)  # Cyan
    elif shape == 'O':
        points = [Point(0, 0), Point(1, 0), Point(0, 1), Point(1, 1)]
        color = (255, 255, 0)  # Yellow
    elif shape == 'T':
        points = [Point(0, 0), Point(-1, 0), Point(1, 0), Point(0, 1)]
        color = (128, 0, 128)  # Purple
    elif shape == 'S':
        points = [Point(0, 0), Point(1, 0), Point(0, 1), Point(-1, 1)]
        color = (0, 255, 0)  # Green
    elif shape == 'Z':
        points = [Point(0, 0), Point(-1, 0), Point(0, 1), Point(1, 1)]
        color = (255, 0, 0)  # Red
    elif shape == 'J':
        points = [Point(0, 0), Point(-1, 0), Point(1, 0), Point(1, 1)]
        color = (0, 0, 255)  # Blue
    elif shape == 'L':
        points = [Point(0, 0), Point(-1, 0), Point(1, 0), Point(-1, 1)]
        color = (255, 165, 0)  # Orange
    else:
        raise ValueError("Forme non reconnue")
    return Tetramino(points,Point(pos,0), color=color)