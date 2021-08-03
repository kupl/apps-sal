from heapq import *


def escape(maze):
    MOVES = {(-1, 0): '^', (1, 0): 'v', (0, -1): '<', (0, 1): '>'}
    direc = {('v^', '^v', '<>', '><'): 'B', ('^<', 'v>', '>^', '<v'): 'L', ('^>', '>v', '<^', 'v<'): 'R'}
    maze = '\n'.join(maze)
    maze = list(map(list, maze.split('\n')))
    X, Y = len(maze) - 1, len(maze[0]) - 1

    for i in range(X + 1):
        for j in ('^', '<', 'v', '>'):
            if j in maze[i]:
                sym = j
                row = i
    x, y = row, maze[row].index(sym)
    xend = (0, X)
    yend = (0, Y)
    q = [(0, sym, (x, y), [])]    # (isEnd,symbol,pos,steps)

    while q and not q[0][0]:
        _, sym, (x, y), S = heappop(q)
        for dx, dy in MOVES:
            pos = a, b = x + dx, y + dy
            if 0 <= a <= X and 0 <= b <= Y and maze[a][b] != '#':
                maze[a][b] = '#'
                steps = S.copy()
                for i in direc:
                    if sym + MOVES[(dx, dy)] in i:
                        steps.append(direc[i])
                        break
                steps.append('F')
                heappush(q, (a in xend or b in yend, MOVES[(dx, dy)], pos, steps))

    return q and q[0][0] and q[0][3]
