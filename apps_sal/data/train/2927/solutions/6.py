def zombie_shootout(zombies, distance, ammo):
    kill = distance * 2
    if kill > ammo < zombies:
        return f'You shot {ammo} zombies before being eaten: ran out of ammo.'
    if kill < zombies:
        return f'You shot {kill} zombies before being eaten: overwhelmed.'
    return f'You shot all {zombies} zombies.'
