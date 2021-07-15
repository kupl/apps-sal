T = int(input())

for _ in range(T):
    ax, ay, bx, by, cx, cy = list(map(int, input().split()))
    mx = min(ax, bx, cx)
    dx = (ax + bx + cx) % 3 - 1
    x = 2 * mx + dx
    my = min(ay, by, cy)
    dy = (ay + by + cy) % 3 - 1
    y = 2 * my + dy
    print((max(abs(x), abs(y)) + (1 if x == y and (mx != 0 or my != 0) else 0)))

