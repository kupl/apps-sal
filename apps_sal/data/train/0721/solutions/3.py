inv = 280000002
mod = 1000000007
for _ in range(int(input())):
    n = int(input())
    if n % 2 == 0:
        n = n // 2 + 1
        a = 2 * ((pow(26, n, mod) - 1) * inv - 1) % mod
        print(a)
    else:
        n = n // 2 + 2
        a = 2 * ((pow(26, n, mod) - 1) * inv - 1) % mod
        a = (a - pow(26, n - 1, mod)) % mod
        print(a)
