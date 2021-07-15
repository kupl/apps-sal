def f(m):
    nonlocal dp, sdp
    l = 0
    for i in range(n):
        while l < n and v[l] < v[i] - m:
            l += 1
        if l - 1 > i - k:
            dp[i] = False
        else:
            dp[i] = (sdp[i - k + 1] != sdp[l - 1])
        sdp[i + 1] = sdp[i] + (1 if dp[i] else 0)
    return dp[n - 1]

n, k = list(map(int, input().split()))
dp = [False for i in range(n + 2)]
sdp = [0 for i in range(n + 2)]
dp[-1] = True
sdp[0] = 1
v = list(map(int, input().split()))
v.sort()
le = -1
r = v[-1] - v[0]
while r - le > 1:
    m = (r + le) // 2
    if f(m):
        r = m
    else:
        le = m  
print(r)

