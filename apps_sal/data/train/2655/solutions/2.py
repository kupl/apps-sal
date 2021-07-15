def duck_shoot(ammo, aim, ducks):
    b = 0
    b += int(aim * ammo)
    return ducks.replace('2','X', b)

