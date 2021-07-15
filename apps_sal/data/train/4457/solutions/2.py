def mega_mind(hp, dps, shots, regen):
    chp = hp
    ans = 0
    while True:
        r = (chp + dps - 1) // dps
        if r <= shots:
            return ans + r
        chp -= (dps * shots - regen)
        ans += shots
        if chp >= hp:
            return -1
