import random
from combat import Combat
class Character(Combat):
    experience = 0
    base_hit_points =10
    attack_limit = 10

    def attack(self):
        roll = random.randint(1,self.attack_limit)
        if self.weapon == 'sword':
            roll +=1
        elif self.weapon == 'axe':
            roll+=2
        return roll >4

    def get_weapon(self):
        weapon_choice = str(input("weapon [S]word, [A]xe, [B]ow"))

        if weapon_choice == "s":
            return 'sword'
        elif weapon_choice == 'a':
            return 'axe'
        elif weapon_choice == 'b':
            return 'bow'
        else:
            return self.get_weapon()


    def __init__ (self, **kwargs):
        self.name = input("name")
        self.weapon = self.get_weapon()
        self.hit_points = self.base_hit_points


    def __str__(self):
        return '{},HP {} , xp {}'.format(self.name,self.hit_points, self.experience)

    def rest(self):
        if self.hit_points < self.base_hit_points:
            self.hit_points +=1

    def leveled_up(self):
        return self.experience >= 5