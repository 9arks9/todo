import random
from characters import Hero, Enemy
from fight import FightModel
from inventory import Weapon

# ===================== MAIN =====================
def main():
    # Hero initialization
    # Hero name, hp, attack, defence, level
    my_hero = Hero('Steve', 100, 5, 5, 1)

    # Enemy initialization
    # Enemy name, hp, attack, defence, level
    rabbit = Enemy('Rabbit', 10, 0.5, 1, 1)      #index 0 in list
    troll = Enemy('Troll', 80, 3, 15, 1)         #index 1 in list
    ogre = Enemy('Ogre', 100, 4, 20, 1)          #index 2 in list
    dragon = Enemy('Dragon', 200, 10, 30, 1)     #index 3 in list
    zombie = Enemy('Zombie', 50, 1, 2, 1)        #index 4 in list
    vampire = Enemy('Vampire', 70, 6, 4, 1)      #index 5 in list
    werewolf = Enemy('Werewolf', 90, 7, 5, 1)    #index 6 in list
    skeleton = Enemy('Skeleton', 40, 5, 3, 1)    #index 7 in list
    goblin = Enemy('Goblin', 60, 2, 10, 1)       #index 8 in list

   ########################################################
#  _______ ______  _____ _______   __________  _   _ ______  #
# |__   __|  ____|/ ____|__   __| |___  / __ \| \ | |  ____| #
#    | |  | |__  | (___    | |       / / |  | |  \| | |__    #
#    | |  |  __|  \___ \   | |      / /| |  | | . ` |  __|   #
#    | |  | |____ ____) |  | |     / /_| |__| | |\  | |____  #
#    |_|  |______|_____/   |_|    /_____\____/|_| \_|______| #
#                                                            #
   ########################################################
                                                           
                                                           

    #
    # randomly select an enemy from the list
    roll = random.randint(0, 8)
    enemy = Enemy.all_monsters[roll]
    #enemy.level_up_monster(1)

    # Fight initialization
    #for i in range(30):
    fight = FightModel(my_hero, enemy) # figh_dungeon, figh_pvp, fight_raid
    print(fight.run())

    # Weapon initialization
    # Weapon name, description, type, value, weight, durability, damage
    # Example weapon
    sword = Weapon('Sword', 'A sharp sword', 'weapon', 10, 5, 100, 15)


if __name__ == "__main__":
    main()