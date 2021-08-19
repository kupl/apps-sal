t = int(input())
for _ in range(t):
    (ax, ay, bx, by, cx, cy) = map(int, input().split())
    (x, y) = (ax + bx + cx, ay + by + cy)
    if x > 0:
        x = x - x // 3 - 1
    else:
        x = x + (2 - x) // 3 - 1
    if y > 0:
        y = y - y // 3 - 1
    else:
        y = y + (2 - y) // 3 - 1
    if x == y == 0:
        print(0)
    elif x == y == 1:
        print(1)
    else:
        print(max(x, -x, y, -y) + int(x == y))
