import sys
def input(): return sys.stdin.readline().rstrip()


def permutation(n, r, mod=10**9 + 7):  # 順列数
    permutation = 1
    for i in range(r):
        permutation = permutation * (n - i) % mod
    return permutation


def combination(n, r, mod=10**9 + 7):  # 組み合わせ数
    r = min(n - r, r)
    bunshi = permutation(n, r, mod)
    bunbo = 1
    for i in range(1, r + 1):
        bunbo = bunbo * i % mod
    return bunshi * pow(bunbo, mod - 2, mod) % mod


def main():
    mod = 10**9 + 7
    mod2 = 998244353
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 1
    for AA in A:
        ans *= AA
        ans %= mod
    sumA = sum(A)
    if sumA > m:
        print(0)
    else:
        nokori = m - sum(A)
        print(combination(m + n, sumA + n, mod=10**9 + 7))


def __starting_point():
    main()


__starting_point()
