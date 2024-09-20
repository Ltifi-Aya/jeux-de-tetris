class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """Ajoute deux points (ou vecteurs de déplacement)."""
        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self):
        """Retourne une représentation en chaîne de caractères """
        return f"Point({self.x}, {self.y})"

    def rotate(self, angle):
        """Retourne un nouveau point obtenu par la rotation du point actuel par un angle donné (en degrés).
           Les angles possibles sont 0, 90, 180, 270."""
        if angle == 0:
            return Point(self.x, self.y)
        elif angle == 90:
            return Point(self.y, -self.x)
        elif angle == 180:
            return Point(-self.x, -self.y)
        elif angle == 270:
            return Point(-self.y, self.x)

    def to_tuple(self):
        """Retourne les coordonnées du point sous forme de tuple."""
        return (self.x, self.y)
