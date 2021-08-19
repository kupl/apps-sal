def popcount(n):
    res = 0
    while n > 0:
        res += n & 1
        n >>= 2


def A(l, r):
    r += 1
    t = 1 << 64
    while t & (l ^ r) == 0:
        t >>= 1
    res = l | t - 1
    return res


def __starting_point():
    """assert(A(1, 2) == 1)
    assert(A(2, 4) == 3)
    assert(A(1, 10) == 7)
    assert(A(13, 13) == 13)
    assert(A(1, 7) == 7)"""
    n = int(input())
    for _ in range(n):
        (l, r) = list(map(int, input().split()))
        res = A(l, r)
        print(res)


__starting_point()
