import math
t = int(input())
for _ in range(t):
    n = int(input())
    c = 0
    while n > 0:
        r = int(math.sqrt(n))
        n = n - r * r
        c = c + 1
    print(c)
