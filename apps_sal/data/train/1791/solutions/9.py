from collections import deque

derp = {'^': (-1, 0),
        '<': (0, -1),
        'v': (+1, 0),
        '>': (0, +1)}


def turn(d1, d2):
    m1, m2 = derp[d1], derp[d2]
    if m1[0] + m2[0] == 0 and m1[1] + m2[1] == 0:
        return 'B'
    if m2[0] - m1[0] + m2[1] + m1[1] == 0:
        return 'L'
    return 'R'


def neighs(maze, pos):
    i, j, d = pos
    mi, mj = derp[d]
    ni, nj = (i + mi, j + mj)
    return [(ni, nj, d)] + [(i, j, nd) for nd in derp.keys() - {d}]


def escape(maze):
    pos = next(((i, j, cell) for i, row in enumerate(maze)
                for j, cell in enumerate(row)
                if cell in derp))

    q = deque([pos])
    prev = {pos: None}
    while q:
        i, j, d = pos = q.popleft()

        try:
            if i < 0 or j < 0:
                raise IndexError
            cell = maze[i][j]
        except IndexError:
            rpath = []
            while True:
                pp = prev[pos]
                if pp is None:
                    break
                (_, _, d1), (_, _, d2) = pp, pos
                if d1 == d2:
                    rpath.append('F')
                else:
                    rpath.append(turn(d1, d2))
                pos = pp
            return rpath[::-1]

        if cell == '
        continue

        for n in neighs(maze, pos):
            if n not in prev:
                i, j, d = n
                q.append(n)
                prev[n] = pos

    return []
