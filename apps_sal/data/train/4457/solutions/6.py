import math

def mega_mind(hp, dps, shots, regen):
    if regen - dps * shots >= 0 and hp - dps * shots > 0:
        return -1
    if hp - dps * shots <= 0:
        return math.ceil(hp / dps)
    n = 0
    while hp - dps * shots > 0:
        hp -= (dps * shots - regen)
        n += 1
    return math.ceil(hp / dps) + n * shots
