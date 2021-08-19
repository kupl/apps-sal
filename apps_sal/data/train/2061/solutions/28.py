t = int(input())
for _ in range(t):
    (ax, ay, bx, by, cx, cy) = map(int, input().split())
    x = ax + bx + cx
    y = ay + by + cy
    (xv, xp) = divmod(x, 3)
    (yv, yp) = divmod(y, 3)
    nx = xv * 2 + xp - 1
    ny = yv * 2 + yp - 1
    if nx == ny:
        if nx == 0:
            print(0)
        elif nx == 1:
            print(1)
        else:
            print(abs(nx) + 1)
    else:
        print(max(abs(nx), abs(ny)))
