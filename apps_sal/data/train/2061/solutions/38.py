from queue import deque


def move(ku):
    x, y, dx, dy = ku
    return (
        (x + dx, y + dy, -dx, -dy),
        (x, y, -dx, dy),
        (x, y + dy, -dx, -dy),
        (x, y + dy, dx, -dy),
        (x, y, dx, -dy),
        (x + dx, y, -dx, dy),
        (x + dx, y, -dx, -dy),
    )


def calc(x, y, dx, dy):
    if dx == 1 and dy == 1:
        if x == 0 and y == 0:
            return 0
        elif x == y:
            return abs(x) * 2 + 1
        else:
            return max(abs(x), abs(y)) * 2
    elif dx == -1 and dy == 1:
        if x == 0 and y == 0:
            return 1
        elif abs(x) - abs(y) == 0:
            if x < 0:
                return abs(x) * 2 + 1
            else:
                return abs(y) * 2
        elif abs(x) - abs(y) < 0:
            return abs(y) * 2
        else:
            if x < 0:
                return abs(x) * 2 + 1
            else:
                return abs(x) * 2 - 1
    elif dx == 1 and dy == -1:
        if y <= 0:
            if abs(x) - abs(y) <= 0:
                return abs(y) * 2 + 1
            else:
                return abs(x) * 2
        else:
            if abs(x) - abs(y) < 0:
                return abs(y) * 2 - 1
            else:
                return abs(x) * 2
    else:
        if x == 0 and y == 0:
            return 2
        elif x == 1 and y == 1:
            return 1
        elif y < 0:
            if x < 0:
                if abs(x) - abs(y) == 0:
                    return abs(x) * 2 + 2
                elif abs(x) - abs(y) < 0:
                    return abs(y) * 2 + 1
                else:
                    return abs(x) * 2 + 1
            else:
                if abs(x) - abs(y) == 0:
                    return abs(x) * 2 + 1
                elif abs(x) - abs(y) < 0:
                    return abs(y) * 2 + 1
                else:
                    return abs(x) * 2 - 1
        else:
            if x < 0:
                if abs(x) - abs(y) < -1:
                    return abs(y) * 2 - 1
                else:
                    return abs(x) * 2 + 1
            else:
                if abs(x) - abs(y) == 0:
                    return abs(x) * 2
                elif abs(x) - abs(y) < 0:
                    return abs(y) * 2 - 1
                else:
                    return abs(x) * 2 - 1


T = int(input())

for _ in range(T):
    ax, ay, bx, by, cx, cy = list(map(int, input().split()))

    if ax == bx:
        gx = ax
    elif bx == cx:
        gx = bx
    else:
        gx = cx

    if ay == by:
        gy = ay
    elif by == cy:
        gy = by
    else:
        gy = cy

    xs = [ax, bx, cx]
    xs.remove(gx)
    xs.remove(gx)

    ys = [ay, by, cy]
    ys.remove(gy)
    ys.remove(gy)

    dx = xs[0] - gx
    dy = ys[0] - gy

#	goal = (gx, gy, dx, dy)

    print((calc(gx, gy, dx, dy)))
