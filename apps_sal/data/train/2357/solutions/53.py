def main():
    mod = 1000000007
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    s = sum(A)
    if s > m:
        return 0
    ans = 1
    inv = 1
    for i in range(s + n):
        ans *= m + n - i
        inv *= i + 1
        ans %= mod
        inv %= mod
    return ans * pow(inv, mod - 2, mod) % mod


def __starting_point():
    print(main())


__starting_point()
