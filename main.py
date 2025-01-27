import time
import title_text as _text
import events as _event
import advanced_random as adv_random
import os
import random

opening_file = 'opening.txt'
text_speed = 0.02
day = 1
skip_intro = True

random_event_chance = 10

virus_spread_chance = 20
virus_recover_chance = 25
virus_death_chance = 5

injury_recover_chance = 40

mortal_wound_recover_chance = 10
mortal_wound_death_chance = 40


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def play():
    if not skip_intro:
        print_from_file(opening_file)
        _print(_text.omega_couriers, print_by_line=True)
        time.sleep(2)
    display_menu('game_menu')


def random_event():
    _event.events[random.choice(list(_event.events.keys()))]()
    input("PRESS ENTER TO CONTINUE")
    clear_console()


def do_ailments():
    ''' Calculates consequences for all crew ailments.'''
    for crewmate in _event.crew:
        if crewmate.infected:
            roll = adv_random.roll_outcome({"spread": virus_spread_chance,
                                            "recover": virus_recover_chance,
                                            "die": virus_death_chance})
            if roll == "spread":              
                _event.virus()
                print(f"{crewmate.name.title()} is infected.")
            elif roll == "recover":
                crewmate.infected = False
                print(f"{crewmate.name.title()} has recovered from their illness.")
            elif roll == "die":
                _event.crew.remove(crewmate)
                print(f"{crewmate.name.title()} has succumbed to their illness.")
            else:
                print(f"{crewmate.name.title()} is infected.")
        if crewmate.injured:
            roll = adv_random.roll_outcome({"recover": injury_recover_chance,})
            if roll == "recover":
                crewmate.injured = False
                print(f"{crewmate.name.title()} has recovered from their injury.")
            else:
                print(f"{crewmate.name.title()} is injured.")
        if crewmate.dying:
            roll = adv_random.roll_outcome({"recover": mortal_wound_recover_chance,
                                            "die": mortal_wound_death_chance})
            if roll == "recover":
                crewmate.dying = False
                print(f"{crewmate.name.title()} has miraculously recovered from their mortal wounds.")
            elif roll == "die":
                _event.crew.remove(crewmate)
                print(f"{crewmate.name.title()} has succumbed to their injuries.")
            else:
                print(f"{crewmate.name.title()} is mortally wounded.")


def game_over():
    print("You died!")
    exit()


def check_game_over():
    if len(_event.crew) > 0:
        return
    else:
        game_over()


def end_day():
    global day
    _print("You head to bed.")
    time.sleep(0.5)
    day += 1
    do_ailments()
    random_event() 


def view_crew():
    for crewmate in _event.crew:
        print(f" - {crewmate}")


def kill_crew():
    _event.crew.clear()


menus = {
    "main_menu": {
        "play": play,
        #"how to play": tutorial,
        #"credits": credits_menu,
    },
    "game_menu": {
        "end day": end_day,
        "assess crew": view_crew,
        "kill": kill_crew
    },
}

def display_menu(current_menu):
    ''' Displays the menu's options and lets the player pick one. Then,
        it executes the corresponding function. current_menu is the menu
        it will open from the menu dictionary.'''
    while True:
        if current_menu == 'main_menu':
            _print(_text.game_title, delay=0.08, print_by_line=True)
        else:
            print(f"It is day {day}.\n")
        num = 1
        for option in menus[current_menu]:
            print(f"{num}. {option.title()}")
            num += 1
        print(f"{num}. Quit")
        choice = input("Choice: ").lower()
        try:
            choice = list(menus[current_menu].keys())[int(choice)-1]
        except Exception:
            pass
        if choice in menus[current_menu]:
            clear_console()
            menus[current_menu][choice]()
        elif choice == 'quit' or choice == str(num):
            return
        else:
            clear_console()


def _print(text: str, delay=text_speed, newline=True, print_by_line=False):
    ''' Function prints text with a typing effect. newline determines
        if the next text will be on a new line, and print_by_line
        determines if it will print by character or print by line.'''
    if delay != 0.0:
        if print_by_line:
            text = text.splitlines()
        for char in text:
            print(char + '\n' * print_by_line, end='', flush=True)
            time.sleep(delay)
        if newline:
            print()
    else:
        print(text, flush=not newline)


def print_from_file(file):
    try:
        with open (file, 'r') as f:
            lines = f.readlines()
            print("PRESS ENTER TO CONTINUE:")
            for line in lines:
                _print(line, newline=False)
                input()
    except FileNotFoundError:
        print(f"ERROR: Could not find {file}")


def main():
    while True:
        display_menu('main_menu')
        confirm = input("Are you sure you want to quit? (y/n) ").lower()
        if 'y' in confirm:
            break


# Main ------------------------------------------------------------------------
main()
