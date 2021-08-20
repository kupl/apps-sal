for _ in range(int(input())):
    (a, b, c, d) = map(int, input().split())
    if c == d and a != b:
        print('NO')
    elif c == d and a == b:
        print('YES')
    else:
        t = abs(a - b) / abs(c - d)
        if t % 1 == 0:
            print('YES')
        else:
            print('NO')
