def form(ax, ay, bx, by, cx, cy):
    P = [(ax, ay), (bx, by), (cx, cy)]
    Q = [(0, 0)]
    for i in range(3):
        x0, y0 = P[i][0], P[i][1]
        x1, y1 = P[(i - 1) % 3][0], P[(i - 1) % 3][1]
        x2, y2 = P[(i + 1) % 3][0], P[(i + 1) % 3][1]
        if abs(x0 - x1) + abs(y0 - y1) == 1 and abs(x0 - x2) + abs(y0 - y2) == 1:
            Q.append(((x1 - x0), (y1 - y0)))
            Q.append(((x2 - x0), (y2 - y0)))
            break
    else:
        return -1
    Q.sort()
    if Q == [(0, 0), (0, 1), (1, 0)]:
        return 11, x0, y0
    elif Q == [(-1, 0), (0, -1), (0, 0)]:
        return 00, x0, y0
    elif Q == [(0, -1), (0, 0), (1, 0)]:
        return 10, x0, y0
    elif Q == [(-1, 0), (0, 0), (0, 1)]:
        return 1, x0, y0


def move(f, x, y):
    if f == 11:
        return [(00, x + 1, y + 1), (10, x, y), (1, x, y), (10, x, y + 1), (00, x, y + 1), (1, x + 1, y), (00, x + 1, y)]
    elif f == 00:
        return [(11, x - 1, y - 1), (1, x, y), (10, x, y), (1, x, y - 1), (11, x, y - 1), (10, x - 1, y), (11, x - 1, y)]
    elif f == 10:
        return [(1, x + 1, y - 1), (11, x, y), (00, x, y), (11, x, y - 1), (1, x, y - 1), (00, x + 1, y), (1, x + 1, y)]
    elif f == 1:
        return [(10, x - 1, y + 1), (00, x, y), (11, x, y), (00, x, y + 1), (10, x, y + 1), (11, x - 1, y), (10, x - 1, y)]


def same_angle(f0, x0, y0, f1, x1, y1):
    if x1 >= x0 and y1 >= y0 and (f0 == f1 == 11 or f0 == f1 == 00):
        return 1
    if x1 < x0 and y1 >= y0 and (f0 == f1 == 1 or f0 == f1 == 10):
        return 1
    if x1 >= x0 and y1 < y0 and (f0 == f1 == 1 or f0 == f1 == 10):
        return 1
    if x1 < x0 and y1 < y0 and (f0 == f1 == 11 or f0 == f1 == 00):
        return 1
    return 0


def next_set(f, x, y):
    P = [(f, x, y)]
    res = [(f, x, y, 0)]
    for t in range(2):
        Q = []
        for f, x, y in P:
            Q.extend(move(f, x, y))
        P = Q
        for f, x, y in P:
            res.append((f, x, y, t + 1))
    return res


def main():
    ax, ay, bx, by, cx, cy = list(map(int, input().split()))
    res = float("inf")
    f, x, y = form(ax, ay, bx, by, cx, cy)
    for f0, x0, y0, time0 in next_set(11, 0, 0):
        for f1, x1, y1, time1 in next_set(f, x, y):
            if same_angle(f0, x0, y0, f1, x1, y1) and max(abs(x0 - x1), abs(y0 - y1)) > 0:
                continue
            if f0 == f1:
                tmp = max(abs(x0 - x1), abs(y0 - y1)) * 2 + (time0 + time1)
                if res > tmp:
                    res = tmp
    print(res)


T = int(input())
for _ in range(T):
    main()
