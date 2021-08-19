T = int(input())
for i in range(T):
    a = int(input())
    s = bin(a)
    d2 = len(s) - s.index('1')
    if 2 ** (d2 - 1) == a:
        d2 -= 1
    d1 = 0
    while d1 * a >= 2 ** d1 - 1:
        d1 += 1
    print(d1 - 1, d2)
