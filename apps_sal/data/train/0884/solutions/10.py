for _ in range(int(input())):
    (x, r) = list(map(int, input().split(' ')))
    m = []
    c = 0
    d = 0
    for i in range(2, x + 1):
        if x % i == 0:
            m.append(i)
            c = c + i ** r
    l = []
    for i in range(2, r + 1):
        if r % i == 0:
            l.append(i)
            d = d + i * x
    print(c, d)
