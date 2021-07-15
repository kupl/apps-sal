from math import ceil, floor


def angle(a, b, c, d, e, f):
    res = []
    if a != c and b != d:
        center = (e, f)
        p = (a, b)
        q = (c, d)
    elif a != e and b != f:
        center = (c, d)
        p = (a, b)
        q = (e, f)
    else:
        center = (a, b)
        p = (c, d)
        q = (e, f)

    if center[0] == p[0]:
        if center[0] > q[0]:
            res.append("r")
        else:
            res.append("l")
    elif center[0] == q[0]:
        if center[0] > p[0]:
            res.append("r")
        else:
            res.append("l")
    if center[1] == p[1]:
        if center[1] < q[1]:
            res.append("d")
        else:
            res.append("u")
    elif center[1] == q[1]:
        if center[1] < p[1]:
            res.append("d")
        else:
            res.append("u")
    return res


def test():
    ax, ay, bx, by, cx, cy = map(int, input().split())
    if set([(ax, ay), (bx, by), (cx, cy)]) == set([(0, 0), (0, 1), (1, 0)]):
        return 0
    XX = (ax + bx + cx) / 3
    YY = (ay + by + cy) / 3
    ang = angle(ax, ay, bx, by, cx, cy)
    if XX > 0 and YY > 0:
        x = ceil(XX)
        y = ceil(YY)
        if (x, y) == (1, 1):
            return 1
        if x == y:
            tmp = x * 2 - 1
            if "r" in ang and "u" in ang:
                return tmp + 1
            return tmp
        tmp = (max(x, y) - 1) * 2
        if x > y and "r" in ang:
            return tmp + 1
        elif y > x and "u" in ang:
            return tmp + 1
        return tmp
    elif XX < 0 and YY > 0:
        x = floor(XX)
        y = ceil(YY)
        x = abs(x)
        if x >= y:
            tmp = x * 2 - 1
            if "l" in ang:
                return tmp + 1
            return tmp
        else:
            tmp = (y - 1) * 2
            if "u" in ang:
                return tmp + 1
            return tmp
    elif XX > 0 and YY < 0:
        x = ceil(XX)
        y = floor(YY)
        y = abs(y)
        if y >= x:
            tmp = y * 2 - 1
            if "d" in ang:
                return tmp + 1
            return tmp
        else:
            tmp = (x - 1) * 2
            if "r" in ang:
                return tmp + 1
            return tmp
    else:
        x = floor(XX)
        y = floor(YY)
        x = abs(x)
        y = abs(y)
        if x == y:
            tmp = 2 * x
            if "d" in ang and "l" in ang:
                return tmp + 1
            return tmp
        tmp = max(x, y) * 2 - 1
        if x > y and "l" in ang:
            return tmp + 1
        if y > x and "d" in ang:
            return tmp + 1
        return tmp


t = int(input())
for _ in range(t):
    print(test())
