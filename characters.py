import random
import logs as Logos

class Character:
    def __init__(self, name, hp, attack, defence, level):
        self._name = name
        self._hp = hp
        self._attack = attack
        self._defence = defence
        self._level = level
        

    @property
    def name(self):
        return f'[{self._level}lvl][{self._name}]'
    @property
    def hp(self):
        return self._hp
    @property
    def attack(self):
        return self._attack
    @property
    def defence(self):
        return self._defence
    @property
    def level(self):
        return self._level

    def __str__(self):
        return f'Name: {self.name}\nHP: [{self._hp}]\nAttack: [{self._attack}]\nDefence: [{self._defence}]\nLevel: [{self._level}]\n'
    
    

# ===================== HERO =====================
# Hero class inherits from Character
# It represents the player character in the game
# It has a level up system and experience points
class Hero(Character):
    def __init__(self, name, hp, attack, defence, level, exp=0):
        super().__init__(name, hp, attack, defence, level)
        self._exp = int(exp)

    @property
    def exp(self):
        return self._exp
    
    def level_up(self):
        self._level += 1
        self._hp += 10
        self._attack += 2
        self._defence += 1
        print(f'{self.name} +++LEVELED UP! STATS BOOSTED!')

    def add_exp(self, value,exp_needed=100):
        self._exp += value

        if self._exp >= exp_needed:
            self.level_up()
            self._exp = 0
            exp_needed *= 2
            print(f'{self.name} needs {exp_needed} exp to get level{self.level+1}.')

    def __str__(self):
        return super().__str__() + f'Exp: [{self._exp}]'        
        
# ===================== ENEMY =====================
# Enemy class inherits from Character
# It represents the enemies in the game
# It has a list of all monsters and methods to manage their stats
# It also has a method to level up the monsters based on the number of kills
# 
class Enemy(Character):
    all_monsters = []  # class attribute to store all monsters
    def __init__(self, name, hp, attack, defence, level,death_monster_count=0):
        self._original_monster_name = name
        super().__init__(name, hp, attack, defence, level)
        Enemy.all_monsters.append(self)
        self._death_monster_count = int(death_monster_count)

    @property
    def death_monster_count(self):
        return self._death_monster_count

    def death_monster_count_setter(self, value):
        self._death_monster_count = value
    
    def add_death(self,value):
        if self._death_monster_count == 10:
            self.level_up_monster(self._death_monster_count)
        elif self._death_monster_count == 50:
            self.level_up_monster(self._death_monster_count)
        elif self._death_monster_count == 500:
            self.level_up_monster(self._death_monster_count)
        self._death_monster_count += value
   
    def level_multiplier(self, multi):
        self._hp = multi * self._hp
        self._attack = multi * self._attack
        self._defence = multi * self._defence
        self._level = multi

    def level_up_monster(self, kill_count):
        if kill_count == 10:
            self.level_multiplier(5)
            print(f'[{self._original_monster_name}] leveled up! stats boosted!')
            print(f'[{self._original_monster_name}] is drunk and lost his mind!\n____________')
            self._name = 'Drunk ' + self._original_monster_name         
            
        elif 50 <= kill_count < 500:
            self.level_multiplier(10)
            print(f'[{self._original_monster_name}] leveled up! stats boosted!')
            print(f'[{self._original_monster_name}] is angry and ready to fight!\n____________')
            self._name = self._original_monster_name + ' Warrior'

        elif kill_count >= 500:
            self.level_multiplier(15)
            print(f'[{self._original_monster_name}] leveled up! stats boosted!')
            print(f'[{self._original_monster_name}] is a terminator now!\n____________')
            self._name = self._original_monster_name + ' Terminator'
            