from dinosaur import Dinosaur
from robot import Robot


class Battlefield:
    def __init__(self):
        self.dinosaur = Dinosaur('T-Rex', 100)
        self.robot = Robot('Cyborg')

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_victor()

    def display_welcome(self):
        print('\nWelcome to Robot VS Dinosaur!\nOnly one will be victorious!\nWhich one will it be?\n')

    def battle_phase(self):
        while self.robot.health > 0:
            if self.robot.health <= 0:
                print(f'{self.dinosaur.name} has defeated {self.robot.name}')
            self.robot.attack_dinosaur(self.dinosaur)
            self.dinosaur.attack_robot(self.robot)
           
    def battle_phase_two(self):
        if self.robot.health > 0:
            self.robot.attack_dinosaur(self.dinosaur)
        elif self.dinosaur.health > 0:
            self.dinosaur.attack_robot(self.robot)
        else:
            print(f'{self.dinosaur.name} is the winner!')

        
        

    def display_victor(self):
        print(f'{self.dinosaur.name} is victorious!')