mod = 10**9 + 7


def sum(x):
    return x * (x + 1) // 2


def solve():
    a, b = list(map(int, input().split()))
    print((sum(b - 1) * (b * sum(a) + a)) % mod)


solve()
