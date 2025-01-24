import characters as _char

crew = []
crew.append(_char.bob)

def illness():
    print("Everyone died.")
    crew.clear()

events = {
    "illness": illness
}