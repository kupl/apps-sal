def zombie_shootout(zombies, distance, ammo):
    if ammo >= zombies and 2 * distance >= zombies:
        return 'You shot all {} zombies.'.format(zombies)
    elif ammo < zombies and ammo < 2 * distance:
        return 'You shot {} zombies before being eaten: ran out of ammo.'.format(ammo)
    else:
        return 'You shot {} zombies before being eaten: overwhelmed.'.format(2 * distance)
