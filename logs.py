class Logos:
    def __init__(self):
        self._log = []   #1 General log
        self._fight_log = []    #2 Damage dealt in fight with enemy with death event
        self._enemy_death_log = []   #3 Enemy death
        self._enemy_level_up_log = []   #4 Enemy level up
        self._inventory_log = []    #5 Inventory event          
        self._equiped_log = []  #6 Equipped item
        self._level_up_log = []   #7 Hero level up
        self._items_log = []   #8 Item creation
        

    @property
    def log(self):
        return self._log
    #1
    def add_log(self, event_to_add):
        self._log.append(event_to_add)
    #2
    def add_fight_log(self, event_to_add):
        self._fight_log.append(event_to_add)
        self._log.append(event_to_add)
    #3
    def add_enemy_death_log(self, event_to_add):
        self._enemy_death_log.append(event_to_add)
        self._log.append(event_to_add)
    #4
    def add_enemy_level_up_log(self, event_to_add):
        self._enemy_level_up_log.append(event_to_add)
        self._log.append(event_to_add)
    #5
    def add_inventory_log(self, event_to_add):
        self._inventory_log.append(event_to_add)
        self._log.append(event_to_add)
    #6
    def add_equiped_log(self, event_to_add):
        self._equiped_log.append(event_to_add)
        self._log.append(event_to_add)
    #7
    def add_level_up_log(self, event_to_add):
        self._level_up_log.append(event_to_add)
        self._log.append(event_to_add)
    #8
    def add_items_log(self, event_to_add):
        self._items_log.append(event_to_add)
        self._log.append(event_to_add)

    
    def clear_log(self):
        self._log.clear()
        self._fight_log.clear()
        self._enemy_death_log.clear()
        self._enemy_level_up_log.clear()
        self._inventory_log.clear()
        self._equiped_log.clear()
        self._items_log.clear()
        self._level_up_log.clear()()
        print('Log cleared!')
        print('____________________')
    
    def display_fight_log(self):
        for log in self._fight_log:
            print(log)
        print('____________________')

    def display_enemy_death_log(self):
        for log in self._enemy_death_log:
            print(log)
        print('____________________')

    def display_enemy_level_up_log(self):
        for log in self._enemy_level_up_log:
            print(log)
        print('____________________')

    def display_inventory_log(self):
        for log in self._inventory_log:
            print(log)
        print('____________________')

    def display_equiped_log(self):
        for log in self._equiped_log:
            print(log)
        print('____________________')
    
    def display_level_up_log(self):
        for log in self._level_up_log:
            print(log)
        print('____________________')
    
    def display_items_log(self):
        for log in self._items_log:
            print(log)
        print('____________________')

    def display_all_logs(self):
        print('____________________')
        print('Fight log:')
        self.display_fight_log()
        print('Enemy death log:')
        self.display_enemy_death_log()
        print('Enemy level up log:')
        self.display_enemy_level_up_log()
        print('Inventory log:')
        self.display_inventory_log()
        print('Equiped log:')
        self.display_equiped_log()
        print('Items log:')
        self.display_items_log()
        print('Level up log:')
        self.display_level_up_log()()
        print('____________________')
        print('All logs:')
        for log in self._log:
            print(log)
        print('____________________')
        