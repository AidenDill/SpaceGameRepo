import random

class Character:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.infected = False
        self.injured = False
        self.dying = False

    def __str__(self):
        return f"{self.name.title()}: {self.role.title()}"
    

names = ["bob",
         "stephen",
         "john",
         "joseph",
         "michael",
         "robert",
         "mary",
         "grace",
         "anne",
         "kelly"]
roles = ["pilot",
         "engineer",
         "doctor",
         "scientist",
         "soldier",
         "chef",]
    

def generate_character():
    return Character(random.choice(names), random.choice(roles))


def generate_crew(members):
    crew = []
    for i in range(members):
        crew.append(generate_character())
    return crew
    
bob = Character("bob", "pilot")
mary = Character("mary", "engineer")