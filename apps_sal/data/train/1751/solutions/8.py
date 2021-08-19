class Battalion:

    def __init__(self, position, soldiers, hit):
        self.position = position
        self.soldiers = soldiers
        self.hit = hit


def queue_battle(dist, *armies):
    bullets = []
    armies = [list(((s, i) for (i, s) in enumerate(a))) for a in armies]
    battalions = [Battalion(i, list(a), False) for (i, a) in enumerate(armies)]
    while len(battalions) > 1:
        for b in reversed(bullets):
            target = battalions[b[2]]
            b[0] = b[0] + b[1][0]
            if b[0] >= dist:
                if not target.hit:
                    target.soldiers.pop(0)
                    target.hit = True
                bullets.remove(b)
        elim = 0
        for (idx, ba) in enumerate(reversed(battalions)):
            if not ba.soldiers:
                battalions.remove(ba)
                bullets = []
                elim += 1
            elif not ba.hit:
                if elim == 0:
                    if idx == 0:
                        target = 0
                    else:
                        target = len(battalions) - idx
                        if target >= len(battalions):
                            target = 0
                    bullets.append([0, ba.soldiers[0], target])
                ba.soldiers.insert(len(ba.soldiers), ba.soldiers[0])
                ba.soldiers.pop(0)
            ba.hit = False
    if battalions:
        pos = battalions[0].position
        survivors = tuple([s[1] for s in battalions[0].soldiers])
        return (pos, survivors)
    else:
        return (-1, ())
