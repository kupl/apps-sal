for _ in range(int(input())):
    n = int(input())
    loss = 0
    for i in range(n):
        p, q, d = list(map(int, input().split()))
        inc = p + (d / 100) * p
        dec = inc - (d / 100) * inc
        diff = p - dec
        loss += diff * q
    print("{0}".format(loss))
