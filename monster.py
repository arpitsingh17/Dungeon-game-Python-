import random
from combat import Combat
COLORS = ['blue','red','magenta','purple']

class Monster(Combat):
    min_hit_points = 1
    max_hit_points =1
    min_experience = 1
    max_experience = 1
    weapon = 'sword'
    sound = 'roar'

    def __init__(self, **kwargs):
        self.hit_points = random.randint(self.min_hit_points,self.max_hit_points)
        self.experience = random.randint(self.min_experience,self.max_experience)
        self.color =random.choice(COLORS)

    def __str__(self):
        return '{} {}, HP : {}, XP :{}'.format(self.color.title(),
                                               self.__class__.__name__,
                                               self.hit_points,
                                               self.experience)

        #for key, value in kwargs.item():
          #  setattr (self,key,value)

    def battle_cry(self):
        return self.sound.upper()

class Goblin(Monster):
    max_hit_points = 3
    max_experience = 2
    sound = 'squeak'

class Troll(Monster):
    min_hit_points = 3
    max_hit_points = 5
    min_experience = 2
    max_experience = 6
    sound = 'growl'

class Dragon(Monster):
    min_hit_points = 5
    max_hit_points = 10
    min_experience = 6
    max_experience = 10
    sound = 'raaaaar'

