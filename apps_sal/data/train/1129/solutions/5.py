
mod = 1000000007


def power(n, m):
    if m == 0:
        return 1
    if m % 2 == 0:
        temp = power(n, m // 2)
        return temp * temp % mod
    else:
        temp = power(n, m // 2)
        return temp * n * temp % mod


for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    print((n * (n - 1) * power(n - 1, m - 1)) % mod)
