def duck_shoot(ammo, aim, ducks):
    hit = min(int(ammo * aim), ducks.count('2'))
    return ducks.replace('2', 'X', hit)

