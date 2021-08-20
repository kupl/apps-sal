try:
    import math as m
    for _ in range(int(input())):
        n = int(input())
        a = [int(i) for i in input().split()]
        if n == 1:
            print(a[0], 1)
            continue
        g = m.gcd(a[0], a[1])
        for i in range(2, n):
            g = m.gcd(g, a[i])
        s = 0
        for i in a:
            s += i // g
        print(g, s)
except:
    pass
