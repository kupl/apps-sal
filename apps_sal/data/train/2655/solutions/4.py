import math


def duck_shoot(ammo, aim, duck_pool):
    shots = math.floor(ammo * aim)
    return duck_pool.replace('2', 'X', shots)
