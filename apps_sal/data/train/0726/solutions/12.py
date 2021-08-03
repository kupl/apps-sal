for _ in range(int(input())):
    n = int(input())
    a = ''
    for i in range(n):
        s = input()
        a = a + s
    c = 0
    o = 0
    d = 0
    e = 0
    h = 0
    f = 0
    for i in a:
        if i == 'c':
            c += 1
        elif i == 'o':
            o += 1
        elif i == 'd':
            d += 1
        elif i == 'e':
            e += 1
        elif i == 'h':
            h += 1
        elif i == 'f':
            f += 1
    c = c // 2
    e = e // 2
    print(min(c, o, d, e, h, f))
