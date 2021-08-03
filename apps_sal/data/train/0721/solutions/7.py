mod = 10 ** 9 + 7


def f(n):
    k = n + 1 >> 1
    ans = 26 * (pow(26, k, mod) - 1) * pow(25, mod - 2, mod) * 2
    if n % 2:
        ans -= pow(26, k, mod)
    ans %= mod
    return ans


for _ in range(int(eval(input()))):
    n = int(eval(input()))
    print(f(n))
