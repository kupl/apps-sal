direction = 0
x, y = 0, 0


def i_am_here(path):
    nonlocal direction
    nonlocal x, y
    i = 0
    while i < len(path):
        rd = reldir.get(path[i])
        if rd is not None:
            direction = (direction + rd) % 4
            i += 1
        else:
            j = i
            while i < len(path) and path[i].isdigit():
                i += 1
            n = int(path[j:i])
            x += n * dx[direction]
            y += n * dy[direction]
    return [y, x]


reldir = dict(r=1, l=-1, L=2, R=2)
dx = 0, 1, 0, -1
dy = -1, 0, 1, 0
