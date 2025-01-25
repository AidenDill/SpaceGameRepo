import characters as _char
import ship as _ship
import random

crew = []
crew.append(_char.bob)
crew.append(_char.mary)
ship = _ship.kestrel


def random_crewmate():
    try:
        return random.choice(crew)
    except IndexError:
        pass


def virus():
    victim = random_crewmate()
    victim.infected = True
    print(f"{victim} has contracted a mysterious virus.")

events = {
    "virus": virus
}