def hydrate(drink_string):
    glasses = 0
    for word in drink_string.split():
        if word.isdigit():
            glasses += int(word)
    return str(glasses) + ' glass of water' if glasses == 1 else str(glasses) + ' glasses of water'
