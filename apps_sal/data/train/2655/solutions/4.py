import math

def duck_shoot(ammo, aim, duck_pool):
    #your code here
    shots = math.floor(ammo*aim)
    return duck_pool.replace('2','X',shots)

