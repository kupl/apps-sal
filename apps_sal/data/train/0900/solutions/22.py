def bigpow(n, p, m):
    if p == 0:
        return 1
    elif p == 1:
        return n
    elif p % 2 == 0:
        tmp = bigpow(n, p // 2, m)
        return tmp * tmp % m
    else:
        return n * (bigpow(n, p - 1, m) % m) % m


def __starting_point():
    tc = int(input().strip())
    for t in range(tc):
        k = int(input().strip())
        m = int(1000000000.0 + 7)
        ans = 10 * bigpow(2, k - 1, m) % m
        print(ans)


__starting_point()
