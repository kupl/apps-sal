import math


def b(l, s, h):
    o = 0
    for i in l:
        o += math.ceil(i / s)
    if o <= h:
        return True
    else:
        return False


t = int(input())
for z in range(t):
    n, h = map(int, input().split())
    l = list(map(int, input().split()))
    q = 1
    r = max(l)
    while q != r:
        s = (q + r) // 2
        if b(l, s, h):
            r = s
        else:
            q = s + 1
    print(r)
