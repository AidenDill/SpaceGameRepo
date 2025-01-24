import time
import title_text as _text
import random_events as _event
import os
import random

opening_file = 'opening.txt'
text_speed = 0.02
day = 1
skip_intro = True


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


def end_day():
    global day
    _print("You head to bed.")
    time.sleep(0.5)
    day += 1
    random_event()


menus = {
    "main_menu": {
        "play": play,
        #"how to play": tutorial,
        #"credits": credits_menu,
    },
    "game_menu": {
        "end day": end_day,
    },
}

def display_menu(current_menu):
    ''' Displays the menu's options and lets the player pick one. Then,
        it executes the corresponding function. current_menu is the menu
        it will open from the menu dictionary.'''
    while True:
        clear_console()
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
