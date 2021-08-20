T = int(input())


def solve(X, Y):
    if X > 0:
        x = X - int(X / 3)
    else:
        x = X + int((2 - X) / 3)
    x -= 1
    if Y > 0:
        y = Y - int(Y / 3)
    else:
        y = Y + int((2 - Y) / 3)
    y -= 1
    if x == 0 and y == 0:
        return 0
    if x == 1 and y == 1:
        return 1
    ans = max([x, -x, y, -y])
    if x == y:
        ans += 1
    return ans


for i in range(T):
    (ax, ay, bx, by, cx, cy) = list(map(int, input().split()))
    X = ax + bx + cx
    Y = ay + by + cy
    print(solve(X, Y))
