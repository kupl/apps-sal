D = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}

def rpg(field, actions):
    g = [list(x) for x in field]
    HP, Atk, Def, Boss, En = 3, 1, 1, 10, 0
    BC = BK = BH = 0
    px = py = 0
    mechanics = {}

    for i in range(len(g)):
        for j in range(len(g[i])):
            if g[i][j] in '^v<>':
                px, py = i, j
            if g[i][j] == 'M':
                mechanics[(i, j)] = 3

    def move(p, q, c):
        nonlocal BK, BC, BH, Atk, Def
        k = g[q[0]][q[1]]
        if k == 'K':
            BK += 1
        elif k == 'C':
            BC += 1
        elif k == 'X':
            Atk += 1
        elif k == 'S':
            Def += 1
        elif k == 'H':
            BH += 1
        g[q[0]][q[1]], g[p[0]][p[1]] = c, ' '

    def bounds(x, y):
        return 0 <= x < len(g) and 0 <= y < len(g[x])

    def attack(i, j, e):
        nonlocal HP, Def
        k = g[i][j]
        nx, ny = i+D[k][0], j+D[k][1]
        for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
            if bounds(x, y) and g[x][y] in 'DE':
                if not (e == 'A' and x == nx and y == ny):
                    HP -= max({'D': 3, 'E': 2}[g[x][y]] - Def, 0)

    for e in actions:
        if e == 'H':
            if BH <= 0 or HP == 3:
                return None
            BH, HP = BH-1, 3
        attack(px, py, e)
        k = g[px][py]
        if e == 'F':
            ox, oy = px, py
            px, py = px+D[k][0], py+D[k][1]
            if not bounds(px, py) or g[px][py] not in ' CKXSH':
                return None
            move((ox, oy), (px, py), k)
        if e in '^v<>':
            g[px][py] = e
            
        nx, ny = px + D[k][0], py + D[k][1]
        if e == 'K':
            if not bounds(nx, ny):
                return None
            if g[nx][ny] not in '-|' or BK <= 0:
                return None
            g[nx][ny] = ' '
            BK -= 1
        elif e == 'A':
            if not bounds(nx, ny) or g[nx][ny] not in 'DE':
                return None
            if g[nx][ny] == 'E' and Atk >= 1:
                En += 1
                if En % 3 == 0:
                    Atk += 1
                g[nx][ny] = ' '
            elif g[nx][ny] == 'D':
                Boss -= Atk
                if Boss <= 0:
                    g[nx][ny] = ' '
                    break
                HP -= max({'D': 3, 'E': 2}[g[nx][ny]] - Def, 0)
        elif e == 'C':
            if not bounds(nx, ny) or g[nx][ny] != 'M' or BC <= 0:
                return None
            mechanics[(nx, ny)] -= 1
            if mechanics[(nx, ny)] == 0:
                g[nx][ny] = ' '
            BC -= 1
    if HP <= 0:
        return None
    Bag = ['C'] * BC + ['H'] * BH + ['K'] * BK
    return g, HP, Atk, Def, Bag
