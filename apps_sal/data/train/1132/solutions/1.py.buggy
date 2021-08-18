def getdp():
    nonlocal mod, maxx
    for i in range(2, maxx):
        n = 2 * (i - 1) + 1
        n = (n * (n + 1)) // 2
        dp[i] = (dp[i - 1] * n) % mod


mod = 1000000007
maxx = 100001
dp = [1] * maxx
getdp()
t = int(input())
while t > 0:
    n = int(input())
    print(dp[n])
    t -= 1
