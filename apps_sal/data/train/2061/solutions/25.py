def solve(x, y):
    x = x - x // 3 if x > 0 else x + (2 - x) // 3
    y = y - y // 3 if y > 0 else y + (2 - y) // 3
    x -= 1
    y -= 1
    if (x, y) == (0, 0):
        return 0
    if (x, y) == (1, 1):
        return 1
    return max(abs(x), abs(y)) + (1 if x == y else 0)


T = int(input())
for _ in range(T):
    (ax, ay, bx, by, cx, cy) = list(map(int, input().split()))
    print(solve(ax + bx + cx, ay + by + cy))
