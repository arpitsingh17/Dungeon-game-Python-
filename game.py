import sys
from character import Character
from monster import  Dragon, Goblin, Troll


class Game:
    def setup(self):
        self.player = Character()
        self.monsters = [Goblin(), Troll(), Dragon()]
        self.monster =  self.get_next_monster()


    def get_next_monster(self):
        try:
            return self.monsters.pop(0)
        except IndexError:
            return  None

    def monster_turn(self):
        if self.monster.attack():
            print(" {} is attacking ".format(self.monster))
            if input("Dodge Y or N").lower() == 'y':
                if self.player.dodge():
                    print("You dodged the attaack")
                else:
                    print("You got hit anyway!")
                    self.player.hit_points -= 1
            else:
                print("{} hit you for 1 point".format(self.monster))
                self.player.hit_points -=1
        else:
            print("{} is not attaking this turn".format(self.monster))



    def player_turn(self):
        player_choice = input("Attack, Quit, Rest").lower()
        if player_choice == 'a':
            print("You are attacking {}".format(self.monster))
            if self.player.attack():
                if self.monster.dodge():
                    print("{} dodged your attack".format(self.monster))
                else:
                    if self.player.leveled_up():
                        self.monster.hit_points -=2
                    else:
                        self.monster.hit_points -=1
                    print("you hit  {} with your {}".format(self.monster, self.player.weapon))
            else:
                print("you missed")
        elif player_choice == 'r':
            self.player.rest()
        elif player_choice == 'q':
            sys.exit()
        else:
            self.player_turn()



    def cleanup(self):
        if self.monster.hit_points <= 0:
            self.player.experience += self.monster.experience
            print(" you killed {}".format(self.monster))
            self.monster  = self.get_next_monster()



    def __init__(self):
        self.setup()

        while self.player.hit_points and (self.monster or self.monsters):
            print('\n'+'='*20)
            print(self.player)
            self.monster_turn
            print('-'*20)
            self.player_turn()
            self.cleanup()
            print('\n'+'='*20)


        if self.player.hit_points:
            print("You won")
        elif self.monsters or self.monster:
            print("You loose")
        sys.exit()

Game()
