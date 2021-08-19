import math
for i in range(int(input())):
    (p, q) = list(map(int, input().split()))
    c = 0
    h = 0
    while q >= 0:
        if q == 0:
            h += 1
            break
        d = int(math.log2(q + 1))
        if d == 0:
            h += 1
            break
        y = 2 ** d - 1
        q -= y + 1
        if q == -1:
            h += 1
            break
        h += 1
    while p >= 0:
        if p == 0:
            c += 1
            break
        else:
            rem = int(math.log2(p + 1))
            if rem == 0:
                c += 1
                break
            y = 2 ** rem - 1
            p -= y + 1
            if p == -1:
                c += 1
                break
            c += 1
    if c == h:
        print(0, 0)
    if c < h:
        print(1, h - c)
    if c > h:
        print(2, c - h)
