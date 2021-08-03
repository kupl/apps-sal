from itertools import product
from functools import lru_cache


def calc(gamemap):
    @lru_cache(None)
    def calc0(p1, p2):
        (y1, x1), (y2, x2) = p1, p2
        cost = gamemap[y1][x1]
        if p1 != p2:
            cost += gamemap[y2][x2]
        res = 0
        for (dy1, dx1), (dy2, dx2) in moves:
            p1 = (y1 + dy1, x1 + dx1)
            if p1 not in playground:
                continue
            p2 = (y2 + dy2, x2 + dx2)
            if p2 not in playground:
                continue
            r = calc0(p1, p2) if p1 < p2 else calc0(p2, p1)
            if r > res:
                res = r
        return cost + res

    playground = set(product(range(len(gamemap)), range(len(gamemap[0]))))
    moves = list(product(((0, 1), (1, 0)), repeat=2))
    return calc0((0, 0), (0, 0))
