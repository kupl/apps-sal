def count(x, y, p, q):
    res = 0
    if x == 0 and y == 0:
        if p == -1 and q == -1:
            return 0
        else:
            return 1
    if x == 0 or y == 0:
        if y == 0:
            x, y = y, x
            p, q = q, p
        if y > 0:
            res += 2 * y
            if q == +1:
                res += 1
        if y < 0:
            res += -2 * y - 1
            if q == -1:
                res += 1
        return res
    p0, q0 = -1, -1
    if x < 0:
        x = -x
        p = -p
        p0 = -p0
    if y < 0:
        y = -y
        q = -q
        q0 = -q0
    if x > y:
        x, y = y, x
        p, q = q, p
        p0, q0 = q0, p0

    res += 2 * x
    if x == y:
        if p0 * q0 == -1 and p * q == -1:
            if p0 != p or q0 != q:
                res += 1
        if p0 + q0 == -2:
            res += 1
        if p + q == 2:
            res += 1
        return res
    if p0 + q0 == -2:
        res += 1
    if p0 == 1 and q0 == -1:
        res += 1
    res += 2 * (y - x) - 1
    if q == +1:
        res += 1
    return res


T = int(input())
xy = [list(map(int, input().split())) for _ in range(T)]

for t in range(T):
    ax, ay, bx, by, cx, cy = xy[t]
    x = sum(list(set([ax, bx, cx])))
    y = sum(list(set([ay, by, cy])))
    if (ax + bx + cx) / 3 - x / 2 > 0:
        p = 1
    else:
        p = -1
    if (ay + by + cy) / 3 - y / 2 > 0:
        q = 1
    else:
        q = -1
    ans = count((x - 1) // 2, (y - 1) // 2, p, q)
    print(ans)
