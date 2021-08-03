from collections import deque

MOVES = {(-1, 0): 'up', (1, 0): 'down', (0, -1): 'left', (0, 1): 'right'}
STATES = ('<', '>', '^', 'v')


def find_start(m):
    for row in range(len(m)):
        for col in range(len(m[row])):
            if m[row][col] in STATES:
                return (row, col), m[row][col]


def escape(maze):
    stored_path = {}
    maze = [list(x) for x in maze]
    row = len(maze)
    col = len(maze[0])
    start, state = find_start(maze)
    end = []
    queue = deque([start])

    while queue:
        x, y = queue.popleft()

        for dx, dy in list(MOVES.keys()):
            xx = x + dx
            yy = y + dy

            if 0 <= xx < row and 0 <= yy < col and maze[xx][yy] != '#':
                queue.append((xx, yy))
                stored_path[(xx, yy)] = (x, y)
                if(xx == 0 or xx == row - 1) and maze[xx][yy] or (yy == 0 or yy == col - 1 and maze[xx][yy]):
                    end = (xx, yy)
                    break
                maze[xx][yy] = '#'

    if not end:
        return end

    full_path = []
    pos = end
    while pos != start:
        x1, y1 = pos
        pos = stored_path[pos]
        x2, y2 = pos
        full_path.append(MOVES[(x1 - x2, y1 - y2)])

    PATH = full_path[::-1]
    out = []
    for direction in PATH:
        # right
        if state == '>' and direction == 'down':
            out.append('R')
            out.append('F')
            state = 'v'

        elif state == '>' and direction == 'right':
            out.append('F')

        elif state == '>' and direction == 'left':
            out.append('B')
            out.append('F')
            state = '<'

        elif state == '>' and direction == 'up':
            out.append('L')
            out.append('F')
            state = '^'

        # left
        elif state == '<' and direction == 'down':
            out.append('L')
            out.append('F')
            state = 'v'

        elif state == '<' and direction == 'left':
            out.append('F')

        elif state == '<' and direction == 'right':
            out.append('B')
            out.append('F')
            state = '>'

        elif state == '<' and direction == 'up':
            out.append('R')
            out.append('F')
            state = '^'

        # down
        elif state == 'v' and direction == 'down':
            out.append('F')
            state = 'v'

        elif state == 'v' and direction == 'left':
            out.append('R')
            out.append('F')
            state = '<'

        elif state == 'v' and direction == 'right':
            out.append('L')
            out.append('F')
            state = '>'

        elif state == 'v' and direction == 'up':
            out.append('B')
            out.append('F')
            state = '^'

        # up
        elif state == '^' and direction == 'down':
            out.append('B')
            out.append('F')
            state = 'v'

        elif state == '^' and direction == 'left':
            out.append('L')
            out.append('F')
            state = '<'

        elif state == '^' and direction == 'right':
            out.append('R')
            out.append('F')
            state = '>'

        elif state == '^' and direction == 'up':
            out.append('F')

    return out
