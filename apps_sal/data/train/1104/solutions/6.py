mod = 10**9 + 7
for _ in range(int(input())):
    n, k = map(int, input().split())
    if n == 0:
        print(k * (k - 1))
    else:
        ans = 0
        tmp = k // 2
        if k & 1:
            ans += k - 1
        ans += (n + tmp) * (n + tmp) - tmp
        print(ans % mod)
