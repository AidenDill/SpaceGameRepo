import random

def roll_outcome(possibilities):
    cumulative_chance = 0
    for outcome in list(possibilities.items()):
        cumulative_chance += outcome[1]
    if cumulative_chance > 100:
        print("ERROR: Given chances add up to over 100%")
    roll = random.randint(0, 100)
    chance_floor = 0
    for outcome in list(possibilities.keys()):
        chance = possibilities[outcome]
        if chance_floor < roll <= chance:
            return outcome
        else:
            chance_floor += chance
    return None

def roll_chance(chance):
    roll = random.randint(0, 100)
    if roll <= chance:
        return True
    else:
        return False