for _ in range(int(input())):
    (a, b, c, d) = list(map(int, input().split()))
    if a > b:
        e = a - b
    else:
        e = b - a
    if c > d:
        f = c - d
    else:
        f = d - c
    if f != 0:
        if e % f == 0:
            print('YES')
        else:
            print('NO')
    elif e == 0:
        print('YES')
    else:
        print('NO')
