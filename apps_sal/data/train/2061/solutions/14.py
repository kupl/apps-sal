flip = {0: {0: 1, 1: 0, 2: 3, 3: 2}, 1: {0: 3, 1: 2, 2: 1, 3: 0}, 2: {0: 0, 1: 3, 2: 2, 3: 1}}
v = [(0, 0), (1, 0), (1, 1), (0, 1)]


def solve(ax, ay, bx, by, cx, cy):
    points = {(ax, ay), (bx, by), (cx, cy)}
    xm = min(ax, bx, cx)
    ym = min(ay, by, cy)
    rs = 2
    for (i, (vx, vy)) in enumerate(v):
        if (xm + vx, ym + vy) not in points:
            rt = i
            break
    if xm == ym == 0:
        if rt == 2:
            return 0
        else:
            return 1
    if xm < 0:
        xm = -xm
        rs = flip[0][rs]
        rt = flip[0][rt]
    if ym < 0:
        ym = -ym
        rs = flip[1][rs]
        rt = flip[1][rt]
    if xm < ym:
        (xm, ym) = (ym, xm)
        rs = flip[2][rs]
        rt = flip[2][rt]
    if xm == ym:
        res = 2 * xm
        if rs == 2:
            if rt == 0:
                res += 2
            else:
                res += 1
        elif rs in (1, 3):
            if rt in (0, flip[2][rs]):
                res += 1
        elif rt == 0:
            res += 1
    else:
        res = 2 * ym + 1
        res += (xm - ym - 1) * 2
        if rs in (1, 2):
            res += 1
        if rt in (0, 3):
            res += 1
    return res


T = int(input())
ans = []
for i in range(T):
    ans.append(solve(*list(map(int, input().split()))))
print(*ans, sep='\n')
