import math
t = int(input())
for i in range(t):
    n = int(input())
    l = {}
    for j in range(n):
        w, s = input().split()
        s = int(s)
        if w not in l:
            l[w] = [1, 0] if s == 0 else [0, 1]
        else:
            if s == 0:
                l[w][0] += 1
            else:
                l[w][1] += 1
    c = 0
    for i in l.values():
        c += max(i)
    print(c)
