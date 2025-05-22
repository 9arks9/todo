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
    
    def fight_model(hero,enemy):
        enemy_hp = enemy.hp
        enemy_attack = enemy.attack
        enemy_defence = enemy.defence
        hero_hp = hero.hp
        hero_attack = hero.attack
        hero_defence = hero.defence
        e_total_dmg = 0
        h_total_dmg = 0 
        Logos.add_fight_log.append(f'==================== FIGHT STARTED ====================')
# Function to get critical damage multiplier
        def get_critical_damage_multiplier(chance):
            roll = random.randint(1, 100)
            if roll <= chance:
                 return random.randint(2, 5)
            return 1
# Calculate damage with critical hit chance
        def damage_calculator(attack, enemy_defensive):
            crit_chance = 10
            crit = get_critical_damage_multiplier(crit_chance)
            return max((attack * crit) - enemy_defensive, 0)
# Fight loop while both characters are alive
# Hero's turn
        while enemy_hp > 0 and hero_hp > 0:
            h_dmg = damage_calculator(hero_attack, enemy_defence)
            if h_dmg <= 0:
                print(f'{hero.name} missed the attack.')
                #break
            enemy_hp -= h_dmg
            h_total_dmg += h_dmg
            if h_dmg > hero_attack - enemy_defence and h_dmg > 0:
                if h_dmg == enemy_hp:
                    h_dmg = str(h_dmg) + ' finishing'
                else:
                    h_dmg = str(h_dmg) + ' (Critical)'
            if enemy_hp < 0:
                enemy_hp = 0
            print(f'{hero.name} --dealt {h_dmg} damage to-- {enemy.name}.')
            print(f'{enemy.name} HP: {enemy_hp}/{enemy.hp}\n___________')
# Check if enemy is dead
            if enemy_hp <= 0:
                break

# Enemy's turn
            e_dmg = damage_calculator(enemy_attack, hero_defence)
            if e_dmg <= 0:
                print(f'{enemy.name} missed the attack.')
                #break
            hero_hp -= e_dmg
            e_total_dmg += e_dmg
            if e_dmg > enemy_attack - hero_defence and e_dmg > 0:
                if e_dmg > hero_hp:
                    e_dmg = str(e_dmg) + ' finishing'
                else:    
                    e_dmg = str(e_dmg) + ' (Critical)'
            if hero_hp < 0:
                hero_hp = 0
            print(f'{enemy.name} --dealt {e_dmg} damage to-- {hero.name}.')
            print(f'{hero.name} HP: {hero_hp}/{hero.hp}\n___________')
# Display Fight result
        if hero_hp <= 0:
            print(f'{hero.name} is dead.')
        elif enemy_hp <= 0:
            print(f'{enemy.name} is dead.')
            hero.add_exp(enemy.level * 5)
            enemy.add_death(1)
            print(f'{hero.name} gained {enemy.level * 5} experience points.')
        else:
            print('Draw')
        return f'\n**************************************\nHero: {hero.name} dealt {h_total_dmg} damage.\nEnemy: {enemy.name} dealt {e_total_dmg} damage.\n**************************************\n----------------------------------------------------------'

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
            