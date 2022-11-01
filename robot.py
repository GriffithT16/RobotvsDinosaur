from weapon import Weapon

lazer_gun = Weapon('Lazer Gun', 50)

class Robot:
    def __init__(self, name, Weapon):
        self.name = name
        self.health = 250
        self.active_weapon = Weapon

    def attack_dinosaur(self, dinosaur_to_attack):
        self.dinosaur_to_attack = dinosaur_to_attack
        self.active_weapon = lazer_gun
        if self.health > 0:
            print(f'{self.name} attacked {dinosaur_to_attack.name}')
            dinosaur_to_attack.health -= self.active_weapon.attack_power
            print(f'{dinosaur_to_attack.name} health is now {dinosaur_to_attack.health}')
