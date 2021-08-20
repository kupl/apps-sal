def mega_mind(hp, dps, shots, regen):
    if hp > dps * shots and dps * shots <= regen:
        return -1
    res = 0
    num_shots = 0
    if hp > dps * shots:
        num_rounds = (hp - dps * shots) // (dps * shots - regen)
        res = num_rounds * shots
        hp -= num_rounds * (dps * shots - regen)
    while hp > 0:
        hp -= dps
        res += 1
        num_shots += 1
        if hp > 0 and num_shots == shots:
            hp += regen
            num_shots = 0
    return res
