class FightModel:
    def __init__(self, hero, enemy, logger=None):
        self.hero = hero
        self.enemy = enemy
        self.logger = logger
        self.hero_hp = hero.hp
        self.hero_attack = hero.attack
        self.hero_defence = hero.defence
        self.enemy_hp = enemy.hp
        self.enemy_attack = enemy.attack
        self.enemy_defence = enemy.defence
        self.h_total_dmg = 0
        self.e_total_dmg = 0

    def get_critical_damage_multiplier(self, chance):
        roll = random.randint(1, 100)
        if roll <= chance:
            return random.randint(2, 5)
        return 1

    def damage_calculator(self, attack, enemy_defensive):
        crit_chance = 10
        crit = self.get_critical_damage_multiplier(crit_chance)
        return max((attack * crit) - enemy_defensive, 0)

    def run(self):
        if self.logger:
            self.logger.add_fight_log('==================== FIGHT STARTED ====================')
        # Fight loop while both characters are alive
        while self.enemy_hp > 0 and self.hero_hp > 0:
            # Hero's turn
            h_dmg = self.damage_calculator(self.hero_attack, self.enemy_defence)
            if h_dmg <= 0:
                print(f'{self.hero.name} missed the attack.')
            self.enemy_hp -= h_dmg
            self.h_total_dmg += h_dmg
            if h_dmg > self.hero_attack - self.enemy_defence and h_dmg > 0:
                if h_dmg == self.enemy_hp:
                    h_dmg = str(h_dmg) + ' finishing'
                else:
                    h_dmg = str(h_dmg) + ' (Critical)'
            if self.enemy_hp < 0:
                self.enemy_hp = 0
            print(f'{self.hero.name} --dealt {h_dmg} damage to-- {self.enemy.name}.')
            print(f'{self.enemy.name} HP: {self.enemy_hp}/{self.enemy.hp}\n___________')
            if self.enemy_hp <= 0:
                break
            # Enemy's turn
            e_dmg = self.damage_calculator(self.enemy_attack, self.hero_defence)
            if e_dmg <= 0:
                print(f'{self.enemy.name} missed the attack.')
            self.hero_hp -= e_dmg
            self.e_total_dmg += e_dmg
            if e_dmg > self.enemy_attack - self.hero_defence and e_dmg > 0:
                if e_dmg > self.hero_hp:
                    e_dmg = str(e_dmg) + ' finishing'
                else:
                    e_dmg = str(e_dmg) + ' (Critical)'
            if self.hero_hp < 0:
                self.hero_hp = 0
            print(f'{self.enemy.name} --dealt {e_dmg} damage to-- {self.hero.name}.')
            print(f'{self.hero.name} HP: {self.hero_hp}/{self.hero.hp}\n___________')
        # Display Fight result
        if self.hero_hp <= 0:
            print(f'{self.hero.name} is dead.')
        elif self.enemy_hp <= 0:
            print(f'{self.enemy.name} is dead.')
            self.hero.add_exp(self.enemy.level * 5)
            self.enemy.add_death(1)
            print(f'{self.hero.name} gained {self.enemy.level * 5} experience points.')
        else:
            print('Draw')
        return f'\n**************************************\nHero: {self.hero.name} dealt {self.h_total_dmg} damage.\nEnemy: {self.enemy.name} dealt {self.e_total_dmg} damage.\n**************************************\n----------------------------------------------------------'
