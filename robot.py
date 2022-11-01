from weapon import Weapon

lazer_gun = Weapon('Lazer Gun', 50)

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 300
        self.active_weapon = lazer_gun

    def attack_dinosaur(self, dinosaur_to_attack):
        self.dinosaur_to_attack = dinosaur_to_attack
        
        if dinosaur_to_attack.health > 0:
            print(f'{self.name} attacked {dinosaur_to_attack.name}')
            dinosaur_to_attack.health -= self.active_weapon.attack_power
            print(f'{dinosaur_to_attack.name} health is now {dinosaur_to_attack.health}')
