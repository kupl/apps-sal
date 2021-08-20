p = 10 ** 9 + 7
f = [1] * (100000 + 1)
for i in range(1, 100000):
    f[i] = i * f[i - 1]
    if f[i] >= p:
        f[i] = f[i] % p
for _ in range(int(input())):
    (n, x, m) = map(int, input().split())
    a = list(map(int, input().split()))
    pre = [1] * (x + 1)
    for i in range(1, x):
        pre[i] = pre[i - 1] * (m + (i - 1)) * f[i - 1]
        if pre[i] >= p:
            pre[i] = pre[i] % p
        pre[i] = pre[i] // f[i]
    ans = 0
    j = 0
    for i in range(x - 1, -1, -1):
        ans += a[j] * pre[i]
        if ans >= p:
            ans = ans % p
        j += 1
    print(ans)
