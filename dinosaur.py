class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.health = 250
        self.attack_power = attack_power

    def attack_robot(self, robot_to_attack):
        if robot_to_attack.health > 0:
            print(f'{self.name} attacked {robot_to_attack.name}')
            robot_to_attack.health -= self.attack_power
            print(f'{robot_to_attack.name} health is now {robot_to_attack.health}')