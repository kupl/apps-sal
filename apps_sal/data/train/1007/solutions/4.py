import math
t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    res = l[0]
    for i in range(1, n):
        res = math.gcd(res, l[i])
    if res == 1:
        print(n)
    else:
        print(-1)
