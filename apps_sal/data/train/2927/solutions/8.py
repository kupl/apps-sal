def zombie_shootout(zombies, distance, ammo):
    shot = 0
    while distance > 0 and ammo > 0 and zombies > 0:
        zombies -= 1
        ammo -= 1
        distance -= 0.5
        shot += 1

    if zombies == 0:
        return 'You shot all ' + str(shot) + ' zombies.'
    elif distance == 0:
        return 'You shot ' + str(shot) + ' zombies before being eaten: overwhelmed.'
    else:
        return 'You shot ' + str(shot) + ' zombies before being eaten: ran out of ammo.'
