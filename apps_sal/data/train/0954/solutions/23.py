import math
t = int(input())
for _ in range(t):
    n = int(input())
    s = 0
    for i in range(n + 1):
        s += math.pow(i, 3)
    print(int((s * 2) - math.pow(n, 3)))
