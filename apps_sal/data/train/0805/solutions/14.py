import math
T = int(input())
for _ in range(T):
    n = int(input())
    m = -1
    for i in range(n):
        si, pi, vi = map(int, input().split())
        si = si + 1
        dailyProfit = vi * (math.floor(pi / si))
        if dailyProfit > m:
            m = dailyProfit
    print(m)
