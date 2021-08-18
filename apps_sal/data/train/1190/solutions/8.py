t = int(input())
while t != 0:
    n = int(input())
    res = 0
    i = 11
    ct = 0
    while n:
        res += n // 2**i
        n = n % 2**i
        i -= 1
    print(res)
    t = t - 1
