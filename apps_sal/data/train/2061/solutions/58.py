def dp1(x, y):
    if x == 0 and y == 0:
        return 0
    if x == y:
        return 2 * x - 1
    else:
        return (max(x, y) - 1) * 2


def dp2(x, y):
    if x >= y:
        return 2 * x - 1
    else:
        return 2 * y - 2


def dp3(x, y):
    if x == y:
        return 2 * x
    else:
        return 2 * max(x, y) - 1


def dp(x, y):
    if x >= 0 and y >= 0:
        return dp1(x, y)
    if x < 0 and y < 0:
        return dp3(-x, -y)
    if x < 0:
        return dp2(-x, y)
    return dp2(-y, x)


def solve(ax, ay, bx, by, cx, cy):
    a = dp(ax, ay)
    b = dp(bx, by)
    c = dp(cx, cy)
    d = max(a, b, c)
    if d == 0:
        return 0
    count = 0
    if a == d:
        count += 1
    if b == d:
        count += 1
    if c == d:
        count += 1
    if count == 1:
        if a + b + c == 3 * d - 2 and d > 1:
            return d + 1
        else:
            return d
    else:
        return d + 1


def main(in_file):
    f = open(in_file)
    t = int(f.readline())
    for _ in range(t):
        ax, ay, bx, by, cx, cy = [int(x) for x in f.readline().split()]
        print(solve(ax, ay, bx, by, cx, cy))


def __starting_point():
    main(0)


__starting_point()
