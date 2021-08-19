from math import floor
t = int(input())
for _ in range(t):
    n = int(input())
    t = floor((2 * n + 1 / 4) ** 0.5 - 1 / 2)
    nt = t * (t + 1) // 2
    print(int(n - nt))
