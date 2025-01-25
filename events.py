import characters as _char
import ship as _ship
import random
import advanced_random as adv_random

crew = []
crew.append(_char.bob)
crew.append(_char.mary)
ship = _ship.kestrel

injuries = [
    "{victim} dropped a piece of heavy equipment on their foot.",
    "{victim} slipped and injured themselves.",
    "{victim} woke up with mysterious injuries all over them.",
    "{victim} got their hand caught in a door."
]
mortal_wounds = [
    "{victim} got into a horrible welding accident.",
    "{victim} got badly burned in a kitchen fire."
]


def random_crewmate():
    try:
        return random.choice(crew)
    except IndexError:
        pass


def virus():
    victim = random_crewmate()
    if victim.infected != True:
        victim.infected = True
        print(f"{victim.name.title()} has contracted a mysterious virus.")


def injury():
    victim = random_crewmate()
    if victim.injured != True:
        victim.injured = True
        print(random.choice(injuries).replace('{victim}', victim.name.title()))


def mortal_wound():
    victim = random_crewmate()
    if victim.dying != True:
        victim.dying = True
        print(random.choice(mortal_wounds).replace('{victim}', victim.name.title()))

events = {
    "virus": virus,
    "injury": injury,
    "mortal wound": mortal_wound
}