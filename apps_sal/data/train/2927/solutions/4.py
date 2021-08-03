def zombie_shootout(zombies, distance, ammo):
    sa = ammo - zombies
    sd = distance * 2 - zombies
    if sa < 0 or sd < 0:
        if sd > sa:
            return f'You shot {ammo} zombies before being eaten: ran out of ammo.'
        else:
            return f'You shot {distance*2} zombies before being eaten: overwhelmed.'
    return f'You shot all {zombies} zombies.'
