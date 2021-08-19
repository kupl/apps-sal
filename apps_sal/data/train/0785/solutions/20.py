t = int(input())
while t:
    n = int(input())
    A = 0
    x = 0
    y = -1
    tmp = 0
    i = 0
    d = 0
    while A > x or x == 0:
        tmp = y
        A += n
        x += 2 ** i
        y = max(y, A - x)
        if y == tmp and d == 0:
            d = i
        i += 1
    if A != x:
        i -= 1
    print(i, d)
    t -= 1
