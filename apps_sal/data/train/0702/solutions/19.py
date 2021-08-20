for _ in range(int(input())):
    (m, t1, t2) = map(int, input().split())
    f = 0
    (a, b) = (t1, t2)
    c = (t2 - t1) / 3
    if c == int(c) and c <= m:
        print('No')
    else:
        print('Yes')
