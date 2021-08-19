mod = 1000000007
for _ in range(int(input())):
    (n, k) = list(map(int, input().split()))
    if n == 0:
        k -= 1
        print(k * (k + 1) % mod)
    elif k == 1:
        print(n ** 2 % mod)
    else:
        if k % 2 == 0:
            a = k // 2
            b = a - 1
            ans = n ** 2 % mod + a * (2 * n % mod) % mod + b * (b + 1) % mod
        else:
            k -= 1
            a = k // 2
            b = a
            ans = n ** 2 % mod + a * (2 * n % mod) % mod + b * (b + 1) % mod
        print(ans % mod)
