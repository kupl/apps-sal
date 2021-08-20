t = int(input())
mod = 10 ** 9 + 7
for _ in range(t):
    (p, q, r) = map(int, input().strip().split())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    c = list(map(int, input().strip().split()))
    a.sort()
    b.sort
    c.sort()
    ans = 0
    for i in b:
        m = 0
        n = 0
        sum1 = 0
        sum2 = 0
        while m < p and a[m] <= i:
            sum1 += a[m]
            m += 1
        while n < r and c[n] <= i:
            sum2 += c[n]
            n += 1
        ans += (sum1 + m * i) * (sum2 + n * i)
    print(ans % mod)
