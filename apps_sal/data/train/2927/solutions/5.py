def zombie_shootout(zombies, distance, ammo):
    results = {f"You shot all {zombies} zombies.": zombies,
               f"You shot {distance * 2} zombies before being eaten: overwhelmed.": distance * 2,
               f"You shot {ammo} zombies before being eaten: ran out of ammo.": ammo}

    return min(results, key=results.get)
