import math


def angle(x1, B, x2):
    (xb, yb) = B
    a = math.sqrt((xb - x1) ** 2 + yb ** 2)
    b = math.sqrt((xb - x2) ** 2 + yb ** 2)
    c = abs(x2 - x1)
    return math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))


for _ in range(int(input())):
    n = int(input())
    X = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    X.sort()
    (l, r) = (0, len(X) - 1)
    ang = 0
    while l < r:
        ang += angle(X[l], B, X[r])
        l += 1
        r -= 1
    print(ang)
