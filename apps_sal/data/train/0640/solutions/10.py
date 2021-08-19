import math
t = int(input())
for i in range(t):
    (x, y) = list(map(int, input().split()))
    if x == y:
        print(0)
    else:
        a = math.gcd(x, y)
        b = x * y // a
        c = b // x
        d = b // y
        print(c + d - 2)
