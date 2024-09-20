from Plateau import *
def intersection(Tetramino1,Tetramino2):
    l=[]
    t1=Tetramino1.image()
    t2=Tetramino2.image()
    for point in t1 :
        l.append(point.to_tuple())
    for point in t2 :
        l.append(point.to_tuple())
    return len(set(l))!=8
def Game():
    # Création de l'interface et du plateau
    interface = Interface(12, 22, "Tetris")
    plateau = Plateau(interface)

    # Initialisation du timer pour les déplacements automatiques
    timer = Timer(1)  # Intervalles de 1 seconde

    # Initialisation du premier tetramino
    tetramino_en_cours = create_tetramino(random.choice(['I','O','T','S','Z','J','L']),2)
    plateau.ajouter_tetramino(tetramino_en_cours)

    while not plateau.game_over():
        touche = interface.lire_touche()
        if touche is not None:
            if touche == 0:
                if len(plateau.tetraminos)==2:
                    c=plateau.tetraminos[plateau.index].cloner()
                    c.tourner(plateau.largeur - 2)
                    if intersection(c, plateau.tetraminos[(plateau.index + 1) % 2])==False:
                        plateau.tetraminos[plateau.index].tourner(plateau.largeur - 2)
                        if not plateau.peut_bouger(plateau.tetraminos[plateau.index], Point(0, 0)):
                            plateau.tetraminos[plateau.index].tourner(plateau.largeur - 2)
                            plateau.tetraminos[plateau.index].tourner(plateau.largeur - 2)
                            plateau.tetraminos[plateau.index].tourner(plateau.largeur - 2)

                else:
                    plateau.tetraminos[plateau.index].tourner(plateau.largeur - 2)
                    if not plateau.peut_bouger(plateau.tetraminos[plateau.index], Point(0, 0)):
                        plateau.tetraminos[plateau.index].tourner(plateau.largeur - 2)
                        plateau.tetraminos[plateau.index].tourner(plateau.largeur - 2)
                        plateau.tetraminos[plateau.index].tourner(plateau.largeur - 2)
            elif touche == 2:
                if len(plateau.tetraminos)==2:
                    c=plateau.tetraminos[plateau.index].cloner()
                    c.translater(Point(0, 1))
                    if intersection(c,plateau.tetraminos[(plateau.index+1)%2]):
                        if plateau.peut_bouger(plateau.tetraminos[(plateau.index+1)%2], Point(0, 1)):
                            plateau.tetraminos[plateau.index].translater(Point(0, 1))
                            plateau.tetraminos[(plateau.index + 1) % 2].translater(Point(0, 1))
                    elif plateau.peut_bouger(plateau.tetraminos[plateau.index], Point(0, 1)):
                        plateau.tetraminos[plateau.index].translater(Point(0, 1))
                elif plateau.peut_bouger(plateau.tetraminos[plateau.index], Point(0, 1)):
                    plateau.tetraminos[plateau.index].translater(Point(0, 1))
            elif touche == 3:
                if len(plateau.tetraminos)==2:
                    c=plateau.tetraminos[plateau.index].cloner()
                    c.translater(Point(-1, 0))
                    if intersection(c,plateau.tetraminos[(plateau.index+1)%2]):
                        if plateau.peut_bouger(plateau.tetraminos[(plateau.index+1)%2], Point(-1, 0)):
                            plateau.tetraminos[plateau.index].translater(Point(-1, 0))
                            plateau.tetraminos[(plateau.index + 1) % 2].translater(Point(-1, 0))
                    elif plateau.peut_bouger(plateau.tetraminos[plateau.index], Point(-1, 0)):
                        plateau.tetraminos[plateau.index].translater(Point(-1, 0))
                elif plateau.peut_bouger(plateau.tetraminos[plateau.index], Point(-1, 0)):
                    plateau.tetraminos[plateau.index].translater(Point(-1, 0))
            elif touche == 1:
                if len(plateau.tetraminos) == 2:
                    c = plateau.tetraminos[plateau.index].cloner()
                    c.translater(Point(1, 0))
                    if intersection(c, plateau.tetraminos[(plateau.index + 1) % 2]):
                        if plateau.peut_bouger(plateau.tetraminos[(plateau.index + 1) % 2], Point(1, 0)):
                            plateau.tetraminos[plateau.index].translater(Point(1, 0))
                            plateau.tetraminos[(plateau.index + 1) % 2].translater(Point(1, 0))
                    elif plateau.peut_bouger(plateau.tetraminos[plateau.index], Point(1, 0)):
                        plateau.tetraminos[plateau.index].translater(Point(1, 0))
                elif plateau.peut_bouger(plateau.tetraminos[plateau.index], Point(1, 0)):
                    plateau.tetraminos[plateau.index].translater(Point(1, 0))

            elif touche == 4:  # Touche espace pour changer le contrôle
                plateau.index = (plateau.index + 1) % len(plateau.tetraminos)
                print(plateau.index)

        if timer.check():

            for tetramino in plateau.tetraminos:
                if plateau.peut_bouger(tetramino, Point(0, 1)):
                    tetramino.translater(Point(0, 1))
                else:
                    plateau.poser_tetramino(tetramino)
                    if len(plateau.tetraminos) == 1:
                        plateau.index=0

                    if len(plateau.tetraminos) == 0:
                        if plateau.nombre_lignes<2:
                            tetramino_en_cours = create_tetramino(random.choice(['I', 'O', 'T', 'S', 'Z', 'J', 'L']),4)
                            plateau.ajouter_tetramino(tetramino_en_cours)
                        else:
                            tetramino_en_cours = create_tetramino(random.choice(['I', 'O', 'T', 'S', 'Z', 'J', 'L']), 2)
                            plateau.ajouter_tetramino(tetramino_en_cours)
                            tetramino_en_cours2 = create_tetramino(random.choice(['I', 'O', 'T', 'S', 'Z', 'J', 'L']),6)
                            plateau.ajouter_tetramino(tetramino_en_cours2)



        plateau.dessiner()
    print("Game Over")
    print("Score:", plateau.score)
    interface.fermer()


if __name__ == "__main__":
    Game()
