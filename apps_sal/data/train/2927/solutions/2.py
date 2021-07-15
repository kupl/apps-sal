def zombie_shootout(zombies, distance, ammo):
    if distance * 2 < min(ammo+1, zombies):
        return f"You shot {distance*2} zombies before being eaten: overwhelmed."
    if ammo < zombies:
        return f"You shot {ammo} zombies before being eaten: ran out of ammo."
    return f"You shot all {zombies} zombies."
