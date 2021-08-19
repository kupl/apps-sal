def mega_mind(hp, dps, shots, regen):
    if hp > dps * shots and dps * shots <= regen:
        return -1
    total_shot = 0  # Initalize shot counter
    barell = shots  # Initalize first gun
    while hp > 0:
        if hp > dps * shots:  # Machine gun mode
            if barell == 0:  # Reload
                barell += shots
                hp += regen
            else:  # Shoot
                barell -= shots
                hp -= dps * shots
                total_shot += shots
        else:  # Gun mode
            if barell == 0:  # Reload
                barell += shots
                hp += regen
            else:  # Shoot
                barell -= 1
                hp -= dps
                total_shot += 1
    return total_shot
