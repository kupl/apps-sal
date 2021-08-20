mod = 1000000007
t = int(input())
for _ in range(t):
    (m, n) = list(map(int, input().split()))
    x = min(m, n)
    f1 = m * n % mod
    s1 = x * (x - 1) // 2 % mod
    f2 = (m + n) % mod
    s2 = x * (x - 1) * (2 * x - 1) // 6 % mod
    s3 = s1 * s1 % mod
    ans = (f1 * s1 % mod - f2 * s2 % mod + s3) % mod
    print(ans)
