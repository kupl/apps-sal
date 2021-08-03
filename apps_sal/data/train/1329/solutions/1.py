author = "himanshu malhotra"
aa, bb = 0, 0
for _ in range(eval(input())):
    n, m = list(map(int, input().split()))
    li = list(map(int, input().split()))
    dp = [float("inf")] * ((1 << n) + 1)
    for i in range(n):
        dp[1 << i] = li[i]
    dp[1 << (n - 1)] = min(dp[1 << (n - 1)], sum(li))
    for i in range(m):
        q = list(map(int, input().split()))
        cost, no, items = q[0], q[1], q[2:]
        mask = 0
        for j in items:
            mask |= (1 << (j - 1))
        dp[mask] = min(dp[mask], cost)
    for i in range((1 << n) - 1, -1, -1):
        for j in range(n):
            if i & (1 << j):
                dp[i ^ (1 << j)] = min(dp[i ^ (1 << j)], dp[i])
    ans = [float("inf")] * ((1 << n) + 1)
    ans[0] = 0
    for i in range(1 << n):
        submask = i
        while submask > 0:
            ans[i] = min(ans[i], dp[submask] + ans[i - submask])
            submask = (submask - 1) & i
    print(ans[(1 << n) - 1])
