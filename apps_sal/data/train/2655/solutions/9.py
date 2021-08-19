def duck_shoot(ammo, aim, ducks):
    bangs = int(ammo * aim)
    if bangs == 0:
        return ducks
    res = list(ducks)
    shot = 0
    for (i, c) in enumerate(res):
        if c == '2':
            res[i] = 'X'
            shot += 1
            if shot >= bangs:
                break
    return ''.join(res)
