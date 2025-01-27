import characters as _char
import ship as _ship
import random
import advanced_random as adv_random

crew = []
crew.extend(_char.generate_crew(4))
ship = _ship.kestrel

injuries = [
    "{victim} dropped a piece of heavy equipment on their foot.",
    "{victim} slipped and injured themselves fairly badly.",
    "{victim} woke up with mysterious injuries all over them.",
    "{victim} got their hand caught in a door, breaking several of their fingers."
]
mortal_wounds = [
    "{victim}'s welding torch exploded in their hand while they were working.",
    "{victim} got badly burned in a kitchen fire.",
    "{victim} got caught in a spinning fan blade, slicing them open.",
    "A safety railing unexpectedly fell apart while {victim} was leaning on it, causing them to fall several stories.",
    "{victim} suffered a sudden heart attack and fell unconscious.",
    "{victim} suffered a sudden stroke and fell unconscious.",
    "{victim} slipped and smashed their head against a metal storage container, causing severe head trauma."
]
deaths = [
    "While operating heavy machinery, {victim}'s vehicle suddenly began moving on its own, brutally crushing them.",
    "An unfortunate malfunction in the ship's weapon systems caused a localized energy burst in one of the nearby rooms. {victim} was in the wrong place at the wrong time and was instantly vaporized.",
    "For some unknown reason, the ship's reactor suddenly released a radioactive pulse while {victim} was present, instantly boiling them alive.",
    "A stray electrical fault sent a deadly shock through {victim}. They never had a chance to react.",
    "{victim} couldn't deal with the situation. When everyone woke up, {victim} was found hanged in their room."
]


def random_crewmate():
    try:
        return random.choice(crew)
    except IndexError:
        pass


def choose_crewmate():
    while True:
        num = 1
        for crewmate in crew:
            print(f"{num}. {crewmate}")
            num += 1
        choice = input("Who do you choose? ").lower()
        try:
            choice = crew[int(choice)-1]
        except Exception:
            pass
        if choice in crew:
            return choice
        else:
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
        print(f"{victim.name.title()} is now injured.")


def mortal_wound():
    victim = random_crewmate()
    if victim.dying != True:
        victim.dying = True
        print(random.choice(mortal_wounds).replace('{victim}', victim.name.title()))
        print(f"{victim.name.title()} is now in mortal peril.")


def instant_death():
    victim = random_crewmate()
    crew.remove(victim)
    print(random.choice(deaths).replace('{victim}', victim.name.title()))
    print(f"{victim.name.title()} has died.")


def engine_failure():
    print("Your engines failed, leaving you stranded in space.")
    print("You decide to send someone to fix it.")
    choice = choose_crewmate()
    if choice.role == "engineer":
        print(f"{choice.name.title()} puts their engineering skills to use and fixes the engine.")
    else:
        roll = adv_random.roll_outcome({"fix": 50,
                                        "injury": 50})
        if roll == "fix":
            print(f"It may not be the best fix, but {choice.name.title()} manages to get the engine running again.")
        elif roll == "injury":
            choice.injured = True
            print(f"{choice.name.title()} gets the engine working, but burns themselves pretty badly.")


events = {
    "virus": virus,
    "injury": injury,
    "mortal wound": mortal_wound,
    "death": instant_death,
    "engine failure": engine_failure
}