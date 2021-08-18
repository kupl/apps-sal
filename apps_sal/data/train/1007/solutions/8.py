import math
for _ in range(int(input())):
    n = int(input())
    ar = [int(x) for x in input().split()]
    f = 0
    g = ar[0]
    for i in range(1, n):
        g = math.gcd(g, ar[i])
        if g == 1:
            f = 1
            print(n)
            break
    if f == 0:
        print(-1)
