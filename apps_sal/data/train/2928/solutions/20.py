LEFT = 'wpbs'[::-1]
RIGHT = 'mqdz'[::-1]


def sum_points(s):
    return sum([LEFT.find(e) - RIGHT.find(e) for e in s])


def alphabet_war(fight):
    suma = sum_points(fight)
    if suma > 0:
        return 'Left side wins!'
    elif suma < 0:
        return 'Right side wins!'
    else:
        return "Let's fight again!"
