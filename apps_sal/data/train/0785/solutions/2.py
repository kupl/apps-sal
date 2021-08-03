from math import log2, log
for _ in range(int(input())):
    a = int(input())
    d1 = int()
    n = 1
    d2 = int()
    while True:
        if n * a + 1 <= pow(2, n):
            break
        else:
            d1 = n
            n += 1
    n = int(log2(a / log(2)))
    dn = n * a - pow(2, n)
    n += 1
    dn1 = n * a - pow(2, n)
    if dn >= dn1:
        d2 = n - 1
    else:
        d2 = n
    print(d1, d2)
