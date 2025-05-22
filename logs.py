class Logos:
    def __init__(self):
        self._log = ''   #1 General log
        self._fight_log = ''    #2 Damage dealt in fight with enemy with death event
        self._enemy_death_log = ''   #3 Enemy death
        self._enemy_level_up_log = ''   #4 Enemy level up
        self._inventory_log = ''    #5 Inventory event          
        self._equiped_log = ''  #6 Equipped item
        self._level_up_log = ''   #7 Hero level up
        self._items_log = ''   #8 Item creation
        
    @property
    def log(self):
        return self._log
    @property
    def fight_log(self):
        return self._fight_log
    @property
    def enemy_death_log(self):
        return self._enemy_death_log
    @property
    def enemy_level_up_log(self):
        return self._enemy_level_up_log
    @property
    def inventory_log(self):
        return self._inventory_log
    @property
    def equiped_log(self):
        return self._equiped_log
    @property
    def level_up_log(self):
        return self._level_up_log
    @property
    def items_log(self):
        return self._items_log
    @log.setter
    def log(self, value):
        self._log += value + '\n'
    @fight_log.setter
    def fight_log(self, value):
        self._fight_log += value + '\n'
    @enemy_death_log.setter
    def enemy_death_log(self, value):
        self._enemy_death_log += value + '\n'
    @enemy_level_up_log.setter
    def enemy_level_up_log(self, value):
        self._enemy_level_up_log += value + '\n'
    @inventory_log.setter
    def inventory_log(self, value):
        self._inventory_log += value + '\n'
    @equiped_log.setter
    def equiped_log(self, value):
        self._equiped_log += value + '\n'
    @level_up_log.setter
    def level_up_log(self, value):
        self._level_up_log += value + '\n'
    @items_log.setter
    def items_log(self, value):
        self._items_log += value + '\n'
    
        