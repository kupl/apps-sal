only_show_wrong()


def rpg(field: List[List[str]], actions: List[str]) -> Tuple[List[List[str]], int, int, int, List[str]]:
    print(field, actions)
    width = len(field[0])
    height = len(field)
    player = None
    lords = 0
    merchants = {}
    enemies = {}
    for (y, row) in enumerate(field):
        for (x, c) in enumerate(row):
            if c in dirchr:
                if player is None:
                    player = (x, y)
                    direction = dirchr.index(c)
                    field[y][x] = ' '
                else:
                    raise ValueError
            elif c == 'D':
                if lords:
                    raise ValueError
                enemies[x, y] = 10
                lords += 1
            elif c == 'E':
                enemies[x, y] = 1
            elif c == 'M':
                merchants[x, y] = 3
    if not player:
        raise ValueError
    health = 3
    attack = 1
    defense = 1
    bag = []
    killed = 0
    (x, y) = player
    for a in actions:
        if a == 'F':
            health -= check_enemy_attack(field, width, height, x, y, defense)
            x += dx[direction]
            y += dy[direction]
            if x < 0 or x >= width or y < 0 or (y >= height) or (field[y][x] not in ' CKHSX'):
                return None
            obj = field[y][x]
            field[y][x] = ' '
            if obj in 'CKH':
                bag.append(obj)
            elif obj == 'S':
                defense += 1
            elif obj == 'X':
                attack += 1
        elif a in dirchr:
            direction = dirchr.index(a)
            health -= check_enemy_attack(field, width, height, x, y, defense)
        elif a in 'ACKH':
            if a in 'CKH':
                if a not in bag:
                    return None
                bag.remove(a)
            (tx, ty) = (x + dx[direction], y + dy[direction])
            if tx < 0 or tx >= width or ty < 0 or (ty >= width):
                return None
            target = field[ty][tx]
            if a in valid_target and target not in valid_target[a]:
                return None
            if a == 'A':
                enemies[tx, ty] -= attack
                if enemies[tx, ty] <= 0:
                    field[ty][tx] = ' '
                    killed += 1
                    if killed == 3:
                        attack += 1
                        killed = 0
                health -= check_enemy_attack(field, width, height, x, y, defense)
            elif a == 'C':
                merchants[tx, ty] -= 1
                if not merchants[tx, ty]:
                    field[ty][tx] = ' '
            elif a == 'K':
                field[ty][tx] = ' '
            elif a == 'H':
                health = 3
                health -= check_enemy_attack(field, width, height, x, y, defense)
        if health <= 0:
            return None
    field[y][x] = dirchr[direction]
    return (field, health, attack, defense, sorted(bag))


dirchr = '^>v<'
dx = (0, 1, 0, -1)
dy = (-1, 0, 1, 0)
valid_target = dict(A='DE', C='M', K='-|')
enemy_attack = dict(D=3, E=2)


def check_enemy_attack(field, width, height, px, py, defense):
    damage = 0
    for (x, y) in ((px, py - 1), (px + 1, py), (px, py + 1), (px - 1, py)):
        if x >= 0 and x < width and (y >= 0) and (y < height) and (field[y][x] in 'DE'):
            attack = enemy_attack[field[y][x]]
            if attack > defense:
                damage += attack - defense
    return damage
