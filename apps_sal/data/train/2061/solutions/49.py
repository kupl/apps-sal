N, *PQRSTU = [int(_) for _ in open(0).read().split()]
P, Q, R, S, T, U = [PQRSTU[_::len('PQRSTU')] for _ in range(len('PQRSTU'))]


def calc(x1, y1, x2, y2, x3, y3):
    gx = x1 + x2 + x3
    gy = y1 + y2 + y3
    if gx > gy:
        gx, gy = gy, gx
    x, dx = divmod(gx, 3)
    y, dy = divmod(gy, 3)
    if x == y:
        if x == 0:
            ret = 1 - (dx * dy == 1)
        elif x > 0:
            ret = 2 * y + 1 + (dx == dy == 2)
        else:
            ret = -2 * y + (dx * dy == 1)
    elif x + abs(y) < 0:
        ret = -2 * x - (dx == 2)
    else:
        ret = 2 * y + (dy == 2)
    return ret


ans = []
for p, q, r, s, t, u in zip(P, Q, R, S, T, U):
    ans += [calc(p, q, r, s, t, u)]
print(('\n'.join(map(str, ans))))
