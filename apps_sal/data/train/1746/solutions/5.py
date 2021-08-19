only_show_wrong()
player = ['^', 'v', '<', '>']
items = [' ', 'K', 'C', 'H', 'S', 'X']


def rpg(field: List[List[str]], actions: List[str]) -> Tuple[List[List[str]], int, int, int, List[str]]:
    health = 3
    attack = 1
    defense = 1
    killed = 0
    bag = []
    demon_health = 10
    merchant_greed = 3
    for action in actions:
        (cell, x, y, x2, y2) = find_player(field)
        if action == 'F':
            if cell not in items:
                return None
            field[y2][x2] = field[y][x]
            field[y][x] = ' '
            if cell == ' ':
                pass
            elif cell == 'X':
                attack += 1
            elif cell == 'S':
                defense += 1
            else:
                bag.append(cell)
        elif action in player:
            field[y][x] = action
        elif action == 'K':
            if cell not in ['-', '|'] or 'K' not in bag:
                return None
            field[y2][x2] = ' '
            bag.remove('K')
        elif action == 'A':
            if cell not in ['E', 'D']:
                return None
            enemy_health = (demon_health if cell == 'D' else 1) - attack
            if enemy_health <= 0:
                field[y2][x2] = ' '
                if cell == 'E':
                    killed += 1
                    if killed == 3:
                        killed = 0
                        attack += 1
            else:
                demon_health = enemy_health
        elif action == 'C':
            if cell != 'M' or 'C' not in bag:
                return None
            merchant_greed -= 1
            bag.remove('C')
            if merchant_greed == 0:
                field[y2][x2] = ' '
        elif action == 'H':
            if health == 3 or 'H' not in bag:
                return None
            health = 3
            bag.remove('H')
        health = check_enemy_near(field, x, y, health, defense)
        if health <= 0:
            return None
    bag.sort()
    return (field, health, attack, defense, bag)


def check_enemy_near(field, x, y, health, defense):
    w = len(field[0])
    h = len(field)
    for (dx, dy) in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        (x2, y2) = (x + dx, y + dy)
        if 0 <= x2 < w and 0 <= y2 < h:
            if field[y2][x2] == 'E':
                health -= max(0, 2 - defense)
            elif field[y2][x2] == 'D':
                health -= max(0, 3 - defense)
    return health


def get_direction(player):
    if player == '^':
        return (0, -1)
    elif player == 'v':
        return (0, 1)
    elif player == '<':
        return (-1, 0)
    elif player == '>':
        return (1, 0)


def find_player(field):
    w = len(field[0])
    h = len(field)
    for y in range(h):
        for x in range(w):
            if field[y][x] in player:
                (dx, dy) = get_direction(field[y][x])
                (x2, y2) = (x + dx, y + dy)
                return (field[y2][x2] if 0 <= x2 < w and 0 <= y2 < h else None, x, y, x2, y2)
    return (None, 0, 0, 0, 0)
