import math
for _ in range(int(input())):
    n = int(input())
    x = 0
    mi = []
    for i in range(n):
        l = list(map(int, input().split()))
        c = l[0]
        l1 = l[1:]
        d = math.floor(c / 2)
        s = sum(l1[:d])
        x = x + s
        if c % 2 != 0:
            mi.append(l1[d])
    mi.sort(reverse=True)
    for i in range(len(mi)):
        if (i + 1) % 2 != 0:
            x = x + mi[i]
    print(x)
