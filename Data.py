import datetime
from enum import Enum

class Direction(Enum):
    continuer_tout_droit = 1
    faites_demi_tour = 2
    tourner_a_gauche = 3
    tourner_a_droite = 4

class Donnee:
    def __init__(self, direction):
        self.direction = direction