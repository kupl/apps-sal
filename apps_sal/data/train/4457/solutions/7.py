def mega_mind(hp, dps, shots, regen):
    if hp > dps * shots and dps * shots <= regen:
        return -1
    total_shot = 0
    barell = shots
    while hp > 0:
        if hp > dps * shots:
            if barell == 0:
                barell += shots
                hp += regen
            else:
                barell -= shots
                hp -= dps * shots
                total_shot += shots
        else:
            if barell == 0:
                barell += shots
                hp += regen
            else:
                barell -= 1
                hp -= dps
                total_shot += 1
    return total_shot
