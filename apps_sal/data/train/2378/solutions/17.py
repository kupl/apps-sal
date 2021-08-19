q = int(input())
for i in range(q):
    s = str(input())
    (l, r, u, d) = (0, 0, 0, 0)
    for t in s:
        if t == 'L':
            l += 1
        elif t == 'U':
            u += 1
        elif t == 'D':
            d += 1
        else:
            r += 1
    k = min(l, r)
    d = min(u, d)
    if d == 0:
        if k != 0:
            print(2)
            print('LR')
        else:
            print(0)
    elif k == 0:
        if d != 0:
            print(2)
            print('UD')
        else:
            print(0)
    else:
        print(k * 2 + d * 2)
        print('L' * k + 'U' * d + 'R' * k + 'D' * d)
