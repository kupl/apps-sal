from heapq import *
from itertools import starmap
from collections import deque, namedtuple
Army = namedtuple('Army', 'i,q')
Soldier = namedtuple('Soldier', 'i,speed')


def queue_battle(d, *args):
    armies = [Army(i, deque(starmap(Soldier, enumerate(q)))) for (i, q) in enumerate(args)]
    bullets = [[] for _ in range(len(armies))]
    t = 0
    while len(armies) > 1:
        t += 1
        alives = [1] * len(armies)
        for (i, q) in enumerate(bullets):
            if q and q[0] <= t:
                alives[(i + 1) % len(armies)] = 0
            while q and q[0] <= t:
                heappop(q)
        emptyArmies = False
        for (i, alive) in enumerate(alives):
            if alive:
                heappush(bullets[i], t + d / armies[i].q[0].speed)
                armies[i].q.rotate(-1)
            else:
                armies[i].q.popleft()
                emptyArmies |= not armies[i].q
        if emptyArmies:
            armies = [army for army in armies if army.q]
            bullets = [[] for _ in range(len(armies))]
    if not armies:
        return (-1, ())
    win = armies.pop()
    return (win.i, tuple((soldier.i for soldier in win.q)))
