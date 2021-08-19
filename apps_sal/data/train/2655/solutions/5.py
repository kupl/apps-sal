from math import floor


def duck_shoot(ammo, aim, ducks):
    kills = [i for (i, c) in enumerate(ducks) if c == '2'][:min(floor(aim * ammo), ducks.count('2'))]
    return ''.join(['X' if i in kills else c for (i, c) in enumerate(ducks)])
