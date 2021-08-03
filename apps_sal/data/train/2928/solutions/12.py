def alphabet_war(fight):

    left_side = {
        'w': 4,
        'p': 3,
        'b': 2,
        's': 1,
    }

    right_side = {
        'm': 4,
        'q': 3,
        'd': 2,
        'z': 1,
    }

    contador_izq = 0
    contador_dch = 0
    for i in fight:
        if i in left_side.keys():
            contador_izq += left_side[i]
        if i in right_side.keys():
            contador_dch += right_side[i]

    if contador_izq > contador_dch:
        return "Left side wins!"
    elif contador_izq < contador_dch:
        return "Right side wins!"
    else:
        return "Let's fight again!"
