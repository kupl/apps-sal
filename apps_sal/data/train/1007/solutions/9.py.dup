import math


def solve():
    n = int(input())
    l = list(map(int, input().split()))
    g = l[0]
    for i in range(1, len(l)):
        g = math.gcd(g, l[i])
    if g == 1:
        print(n)
    else:
        print(-1)


t = int(input())
i = 0
while i < t:
    solve()
    i += 1
