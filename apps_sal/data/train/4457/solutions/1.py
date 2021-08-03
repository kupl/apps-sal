from math import ceil


def mega_mind(hp, dps, shots, regen):
    if hp > dps * shots <= regen:
        return -1
    n = 0
    while True:
        s = min(int(ceil(hp / dps)), shots)
        n += s
        hp -= dps * s
        if hp <= 0:
            break
        hp += regen
    return n
