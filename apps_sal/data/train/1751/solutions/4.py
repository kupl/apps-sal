def queue_battle(dist, *armies):

    DIST = dist
    ARMY_COUNT = len(armies)

    active_armies = []
    for army in range(0, ARMY_COUNT):
        active_armies.append(army)

    queues = {}
    for n, army in enumerate(armies):
        if n == len(armies) - 1:
            target = 0
        else:
            target = n + 1
        queues[n] = {'target': target, 'army': {k: v for k, v in enumerate(list(army))}}

    bullet_count = 1
    bullets = {}
    no_victor = True

    while no_victor:

        bullets_hit = []
        targets_hit = []

        for bullet, data in bullets.items():
            bullets[bullet]['dist'] += bullets[bullet]['speed']
            if bullets[bullet]['dist'] >= DIST:
                bullets_hit.append(bullet)
                targets_hit.append(bullets[bullet]['target'])

        for bullet in bullets_hit:
            bullets.pop(bullet)

        armies_to_be_removed = []
        for army in queues:
            fk = list(queues[army]['army'].keys())[0]
            if army in targets_hit:
                queues[army]['army'].pop(fk)
                if len(queues[army]['army']) == 0:
                    armies_to_be_removed.append(army)
            else:
                bullets[bullet_count] = {'dist': 0, 'speed': queues[army]['army'][fk], 'target': queues[army]['target']}
                bullet_count += 1
                x = queues[army]['army'][fk]
                queues[army]['army'].pop(fk)
                queues[army]['army'][fk] = x

        if len(armies_to_be_removed) > 0:
            bullets = {}

        for army in armies_to_be_removed:
            active_armies.remove(army)
            queues.pop(army)

        for army in queues:
            if queues[army]['target'] not in active_armies:
                new_target = active_armies.index(army) + 1
                if new_target > len(active_armies) - 1:
                    new_target = 0
                queues[army]['target'] = active_armies[new_target]

        if len(queues) <= 1:
            no_victor = False

    if active_armies == []:
        return (-1, ())
    else:
        winning_army = active_armies[0]
        leftover_soldiers = list(queues[army]['army'].keys())

        return(winning_army, tuple(leftover_soldiers))
