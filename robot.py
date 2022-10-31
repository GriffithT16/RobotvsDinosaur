from weapon import Weapon

class Robot:
    def __init__(self, name, Weapon):
        self.name = name
        self.health = 250
        self.active_weapon = Weapon

    def attack(self, dinosaur):
        pass