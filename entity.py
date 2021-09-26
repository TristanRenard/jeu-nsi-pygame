class Entity:
    def __init__(self, posx: int, posy: int, vitesse: int = 1, agressive = False,):
        self.posx = posx
        self.posy = posy
        self.vitesse = vitesse
        self.timeleft = 180
        self.agressive = False


