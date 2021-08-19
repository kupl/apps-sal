import math
Q = int(input())
for i in range(Q):
    (a, b) = map(int, input().split())
    if a == b:
        print(2 * (a - 1))
    else:
        d = math.isqrt(a * b - 1)
        if d * (d + 1) < a * b:
            print(2 * d - 1)
        else:
            print(2 * d - 2)
