from dinosaur import Dinosaur
from robot import Robot


class Battlefield:
    def __init__(self):
        self.dinosaur = Dinosaur
        self.robot = Robot

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_victor()

    def display_welcome(self):
        print('\nWelcome to Robot VS Dinosaur!\nOnly one will be victorious!\nWhich one will it be?\n')

    def battle_phase(self):
        pass
        
        

    def display_victor(self):
        pass