import math
t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort(reverse=True)
    p = 0
    for i in range(0, n, 2):
        p += l[i]
    print(p)
