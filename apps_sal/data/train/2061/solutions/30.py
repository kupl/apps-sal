# ARC109-D-600
T = int(input())
for _ in range(T):
    ax, ay, bx, by, cx, cy = map(int, input().split())
    if ax == bx:
        x, xx = ax, cx
    if bx == cx:
        x, xx = bx, ax
    if cx == ax:
        x, xx = cx, bx
    if ay == by:
        y, yy = ay, cy
    if by == cy:
        y, yy = by, ay
    if cy == ay:
        y, yy = cy, by
    xx, yy = xx - x, yy - y
    if x == y == 0:
        if xx == yy == 1:
            g = 0
        elif xx * yy == 1:
            g = 2
        else:
            g = 1
    elif x == 0:
        if y > 0:
            g = 2 * y - (yy == -1)
        else:
            g = -2 * y + (yy == -1)
    elif y == 0:
        if x > 0:
            g = 2 * x - (xx == -1)
        else:
            g = -2 * x + (xx == -1)
    elif x > 0 and y > 0:
        if x == y == 1:
            if xx == yy == -1:
                g = 1
            elif -1 in {xx, yy}:
                g = 2
            else:
                g = 3
        elif x == y:
            if -1 in {xx, yy}:
                g = 2 * max(x, y)
            else:
                g = 2 * max(x, y) + 1
        elif x > y:
            if xx == 1:
                g = 2 * x
            else:
                g = 2 * x - 1
        elif y > x:
            x, y, xx, yy = y, x, yy, xx
            if xx == 1:
                g = 2 * x
            else:
                g = 2 * x - 1
    elif x < 0 and y > 0:
        if x + y == 0:
            if xx == 1:
                g = 2 * y
            else:
                g = 2 * y + 1
        if x + y > 0:
            if yy == -1:
                g = 2 * y - 1
            else:
                g = 2 * y
        if x + y < 0:
            if xx == 1:
                g = -2 * x
            else:
                g = -2 * x + 1
    elif x > 0 and y < 0:
        x, y, xx, yy = y, x, yy, xx
        if x + y == 0:
            if xx == 1:
                g = 2 * y
            else:
                g = 2 * y + 1
        if x + y > 0:
            if yy == -1:
                g = 2 * y - 1
            else:
                g = 2 * y
        if x + y < 0:
            if xx == 1:
                g = -2 * x
            else:
                g = -2 * x + 1
    else:
        if x == y:
            if xx == yy == -1:
                g = -2 * x + 2
            else:
                g = -2 * x + 1
        else:
            if x < y:
                if xx == 1:
                    g = -2 * x
                else:
                    g = -2 * x + 1
            if y < x:
                if yy == 1:
                    g = -2 * y
                else:
                    g = -2 * y + 1
    print(g)
