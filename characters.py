class Character:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.infected = False
        self.injured = False

    def __str__(self):
        return f"{self.name.title()}: {self.role.title()}"
    
bob = Character("bob", "pilot")
mary = Character("mary", "engineer")