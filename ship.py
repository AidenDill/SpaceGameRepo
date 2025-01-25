class Ship:
    def __init__(self, name, fuel, food, water, inventory):
        self.name = name
        self.fuel = fuel
        self.food = food
        self.water = water
        self.inventory = inventory
    
    def __str__(self):
        attributes_to_print = {'name': self.name, 
                               'fuel': self.fuel, 
                               'food': self.food, 
                               'water': self.water, 
                               'inventory': self.inventory}
        lines = []
        for attribute in list(attributes_to_print.keys()):
            lines.append(f"{attribute.title()}: {attributes_to_print[attribute]}")
        return '\n'.join(lines)
    
kestrel = Ship('The Kestrel', 100, 100, 100, [])