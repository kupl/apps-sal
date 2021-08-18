for e in range(int(input())):
    c = 0
    num = int(input())
    for i in range(num):
        p, q, r = map(int, input().split())
        x = p + (r / 100) * p
        x -= (r / 100) * x
        c += (p - x) * q
    print("{0:.6f}".format(c))
