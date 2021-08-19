import math
t = int(input())
for _ in range(t):
    n = int(input())
    maxi = 0
    for i in range(n):
        (s, p, v) = map(int, input().split())
        h = math.floor(p / (s + 1))
        profit = h * v
        maxi = max(maxi, profit)
    print(maxi)
