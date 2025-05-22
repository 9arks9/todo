import logs as Logos

class Inventory:
    def __init__(self):
        self._inventory = []
        self._equipped = []


    @property
    def inventory(self):
        return self._inventory

    @property
    def equipped(self):
        return self._equipped
    
    def add_item(self, item):
        if item.type == 'weapon':
            self._weapons.append(item)
        elif item.type == 'armor':
            self._armor.append(item)
        else:
            self._inventory.append(item)


    
class Itemz:
    def __init__(self,name ="item", description = "Item description", type ='Item type', value = 0, weight = 0, durability = 100):
        self._name = name.capitalize()
        self._description = description.capitalize()
        self._type = type.upper()
        self._value = value
        self._weight = weight
        self._durability = durability
        
        
        

    @property
    def name(self):
        return self._name
    @property
    def description(self):
        return self._description
    @property
    def type(self):
        return self._type
    @property
    def value(self):
        return self._value
    @property
    def weight(self):
        return self._weight
    @property
    def durability(self):
        return self._durability
    def __str__(self):
        return f'Name: {self._name}\nDescription: {self._description}\nType: {self._type}\nValue: {self._value}\nWeight: {self._weight}\nDurability: {self._durability}\n'

class Weapon(Itemz):
    _weapon_list = []  # class attribute to store all weapons
    def __init__(self, name, description, type, value, weight, durability=200, damage=1):
        super().__init__(name, description, type, value, weight, durability)
        self._damage = damage
        self._weapon_list.append(self)
        self.item_created_log = f'Item created: {self._name} - {self._description} - {self._type} - {self._value} - {self._weight} - {self._durability} - {self._damage}'

        Logos.add_items_log(self.item_created_log)    # add item created log to the items log

    @property
    def damage(self):
        return self._damage

    def __str__(self):
        return f'Name: {self._name}\nDescription: {self._description}\nType: {self._type}\nValue: {self._value}\nWeight: {self._weight}\nDurability: {self._durability}\nDamage: {self._damage}\n'
    