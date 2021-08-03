def abs(x): return max(x, -x)


t = int(input())
for i in range(t):
    ax, ay, bx, by, cx, cy = list(map(int, input().split()))
    x = ax + bx + cx
    y = ay + by + cy
    xv = x // 3
    xp = x % 3
    yv = y // 3
    yp = y % 3

    nx = xv * 2 + xp - 1
    ny = yv * 2 + yp - 1

    if nx == ny:
        if nx == 1:
            print((1))
        elif nx == 0:
            print((0))
        else:
            print((abs(nx) + 1))
    else:
        print((max(abs(nx), abs(ny))))
