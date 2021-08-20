t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    ma = 0
    l = []
    for i in range(n * 2):
        if ma < p[i]:
            l.append(i)
            ma = p[i]
    l.append(n * 2)
    m = len(l) - 1
    a = [0] * m
    for i in range(m):
        a[i] = l[i + 1] - l[i]
    dp = [0] * (m + 1)
    dp[0] = 1
    for i in range(m):
        dp[i + 1] = dp[i] | dp[i] << a[i]
    if dp[m] >> n & 1:
        print('YES')
    else:
        print('NO')
