from itertools import product


def knights_tour(start, size):
    m = [[0] * size for i in range(size)]
    d = [[0] * size for i in range(size)]
    directions = [1, 2, -1, -2]
    directions = [(y, x) for (y, x) in product(directions, directions) if abs(y) != abs(x)]

    def inside(y, x):
        return not (y < 0 or x < 0 or y >= size or (x >= size)) and m[y][x] == 0

    def search(start, step):
        if step > size ** 2:
            return []
        (y, x) = start
        m[y][x] = 1
        for (yy, xx) in product(range(size), range(size)):
            d[yy][xx] = [(yy + dy, xx + dx) for (dx, dy) in directions if inside(yy + dy, xx + dx)]
        (s, nxt) = min([(len(d[ny][nx]), (ny, nx)) for (ny, nx) in d[y][x]] + [(int(1000000000.0), start)])
        return [start] + search(nxt, step + 1)
    return search(start, 1)
