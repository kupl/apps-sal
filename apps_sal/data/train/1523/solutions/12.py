no = int(input())
alls = list(input().split())
dp = [0] * (no + 1)
if no == 1:
    dp[1] = alls[0]
    print(dp[1])
elif no == 2:
    dp[2] = int(alls[1]) + int(alls[0])
    print(dp[2])
elif no >= 3:
    dp[1] = int(alls[0])
    dp[2] = int(alls[1]) + int(alls[0])
    a = int(alls[0]) + int(alls[1])
    b = int(alls[1]) + int(alls[2])
    c = int(alls[0]) + int(alls[2])
    dp[3] = max(a, b, c)
    for x in range(4, no + 1):
        d = int(dp[x - 2]) + int(alls[x - 1])
        e = int(dp[x - 1])
        f = int(dp[x - 3] + int(alls[x - 2]) + int(alls[x - 1]))
        dp[x] = max(d, e, f)
    print(dp[no])
