def mega_mind(hp, dps, shots, regen):
    if regen < dps * shots or hp <= shots * dps:
        cnt = 0
        while hp > shots * dps:
            hp = hp - shots * dps + regen
            cnt += shots

        for i in range(hp):
            hp = hp - dps
            cnt += 1
            if hp <= 0:
                return cnt
    return -1
