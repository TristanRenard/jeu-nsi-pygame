import entity

entity = entity.Entity

class Player(entity):
    def __init__(self, posx, posy ,vitesse=1):
        self.posx = posx
        self.posy = posy
        self.vitesse = vitesse