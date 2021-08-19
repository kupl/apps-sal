(T, *I) = map(int, open(0).read().split())
for (ax, ay, bx, by, cx, cy) in zip(*[iter(I)] * 6):
    x = ax + bx + cx
    y = ay + by + cy
    dx = abs(x - x // 3 - 1)
    dy = abs(y - y // 3 - 1)
    print(max(dx, dy) + (x == y and x // 3 != 0))
