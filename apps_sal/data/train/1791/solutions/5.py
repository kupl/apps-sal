import re


def escape(maze):
    PLAYER = re.compile("[><^v]")
    MOVE = {
        "D": {
            '>': ['R', 'F'],
            '<': ['L', 'F'],
            '^': ['B', 'F'],
            'v': ['F']
        },
        "U": {
            '>': ['L', 'F'],
            '<': ['R', 'F'],
            '^': ['F'],
            'v': ['B', 'F']
        },

        "R": {
            '>': ['F'],
            '<': ['B', 'F'],
            '^': ['R', 'F'],
            'v': ['L', 'F']
        },

        "L": {
            '>': ['B', 'F'],
            '<': ['F'],
            '^': ['L', 'F'],
            'v': ['R', 'F']
        }
    }

    ymax, xmax = len(maze), len(maze[0])

    # find the player
    for idx, line in enumerate(maze):
        player = PLAYER.search(line)
        if player is not None:
            y, x = idx, player.start()
            stack = [(y, x, maze[y][x], [])]
            break

    s = set()
    while len(stack) != 0:
        (y, x, pos, moves) = stack.pop(0)

        if y == 0 or x == 0 or y == ymax - 1 or x == xmax - 1:
            return moves

        if (y, x) in s:
            continue

        s.add((y, x))
        if y + 1 < ymax and maze[y + 1][x] == ' ':
            stack.append((y + 1, x, "v", moves + MOVE["D"][pos]))
        if y - 1 >= 0 and maze[y - 1][x] == ' ':
            stack.append((y - 1, x, "^", moves + MOVE["U"][pos]))
        if x + 1 < xmax and maze[y][x + 1] == ' ':
            stack.append((y, x + 1, ">", moves + MOVE["R"][pos]))
        if x - 1 >= 0 and maze[y][x - 1] == ' ':
            stack.append((y, x - 1, "<", moves + MOVE["L"][pos]))

    return []
