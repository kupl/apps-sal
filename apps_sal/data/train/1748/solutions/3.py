class Turret:
    def __init__(self, tid, r, c, size, info):
        self.tid = tid
        self.attack = info[1]
        self.targets = set()
        atkRange = info[0]
        for dr in range(-atkRange, atkRange + 1):
            for dc in range(-atkRange, atkRange + 1):
                if dr == 0 and dc == 0:
                    continue
                ra, ca = r + dr, c + dc
                if not(0 <= ra < size and 0 <= ca < size):
                    continue
                if dr * dr + dc * dc <= atkRange * atkRange:
                    self.targets.add((ra, ca))

class Alien:
    def __init__(self, pathIdx, pos, hp):
        self.pathIdx = pathIdx
        self.pos = pos
        self.hp = hp

def tower_defense(grid, _turrets, _wave):
    answer = 0
    size = len(grid)
    lWave = len(_wave)
    wave = _wave[:]
    ones = set()
    turrets, aliens = [], []
    for r, row in enumerate(grid):
        for c, square in enumerate(row):
            if square == "1":
                ones.add((r, c))
            elif square.isalpha():
                turrets.append(Turret(square, r, c, size, _turrets[square]))
            elif square == "0":
                start = (r, c)
    for turret in turrets:
        turret.targets = turret.targets & (ones | {start})
    turrets.sort(key = lambda t: t.tid)
    path = [start]
    r, c = start
    while ones:
        for r1, c1 in ones:
            if abs(r1 - r) + abs(c1 - c) == 1:
                path.append((r1, c1))
                ones.discard((r1, c1))
                r, c = r1, c1
                break
    lPath = len(path)
    time = -1
    while time < lWave or aliens:
        time += 1
        for i in range(len(aliens) - 1, -1, -1):
            alien = aliens[i]
            if alien.hp <= 0:
                del aliens[i]
                continue
            alien.pathIdx += 1
            if alien.pathIdx == lPath:
                answer += alien.hp
                del aliens[i]
                continue
            alien.pos = path[alien.pathIdx]
        if time < lWave:
            hp = wave[time]
            if hp > 0:
                aliens.append(Alien(0, path[0], hp))
        for turret in turrets:
            turret.shots = turret.attack
        shot = True
        while shot:
            shot = False
            for turret in turrets:
                if turret.shots > 0:
                    for alien in aliens:
                        if alien.hp <= 0:
                            continue
                        if alien.pos not in turret.targets:
                            continue
                        alien.hp -= 1
                        turret.shots -= 1
                        shot = True
                        break
    return answer
