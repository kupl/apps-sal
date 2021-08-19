for _ in range(int(input())):
    (a, b) = list(map(int, input().split()))
    c = list(bin(a + 1)[2:])
    d = list(bin(b + 1)[2:])
    e = c.count('1')
    f = d.count('1')
    if e == f:
        print(0, 0)
    elif e < f:
        print(1, f - e)
    else:
        print(2, e - f)
