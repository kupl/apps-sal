for _ in range(int(input())):
    l, r, u, d = 0, 0, 0, 0
    s = list(input())
    for i in s:
        if i == 'L':
            l += 1
        elif i == 'R':
            r += 1
        elif i == 'U':
            u += 1
        else:
            d += 1
    d = min(d, u)
    r = min(r, l)
    if d == 0 and r == 0:
        print(0)
    elif d != 0 and r != 0:
        print(2 * (d + r))
        print(d * 'U' + r * 'R' + d * 'D' + r * 'L')
    else:
        print(2)
        if d == 0:
            print('LR')
        else:
            print('UD')
