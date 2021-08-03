from collections import deque, namedtuple, defaultdict

Army = namedtuple('Army', ('num', 'soldiers'))
Soldier = namedtuple('Soldier', ('num', 'speed'))


def queue_battle(distance, *armies):
    bullets = defaultdict(set)
    now = 0
    armies = [Army(an, deque(Soldier(sn, sp) for sn, sp in enumerate(army)))
              for an, army in enumerate(armies)]

    while len(armies) > 1:
        now += 1

        fallen = bullets.pop(now, {})
        eliminated = []
        for ai in fallen:
            armies[ai].soldiers.popleft()
            if not armies[ai].soldiers:
                eliminated.append(ai)

        for ai, army in enumerate(armies):
            if ai in fallen:
                continue
            target = (ai + 1) % len(armies)
            ttime = now + 1 + (distance - 1) // army.soldiers[0].speed
            bullets[ttime].add(target)
            army.soldiers.rotate(-1)

        if eliminated:
            armies = [army for ai, army in enumerate(armies) if ai not in eliminated]
            bullets.clear()

    if armies:
        return armies[0].num, tuple(s.num for s in armies[0].soldiers)
    else:
        return -1, ()
