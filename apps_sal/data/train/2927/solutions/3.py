def zombie_shootout(zombies, range, ammo):
    distance = range * 2
    if zombies > ammo < distance:
        return f"You shot {ammo} zombies before being eaten: ran out of ammo."
    elif zombies > distance:
        return f"You shot {distance} zombies before being eaten: overwhelmed."
    return f"You shot all {zombies} zombies."
