mod = 1000000007
dp = []
dp.append(1)
tens = []
tens.append(10)
tws = []
tws.append(1)
for i in range(1, 21):
    tens.append(tens[i - 1] * tens[i - 1])
    dp.append(dp[i - 1] * tens[i - 1] + dp[i - 1])
    tws.append(tws[i - 1] * 2)
t = eval(input())
t = int(t)
for i in range(0, t):
    now = 0
    (b, a) = input().split()
    a = int(a)
    b = int(b)
    j = 20
    val = 0
    while j >= 0:
        if b >= tws[j]:
            val *= tens[j]
            val += dp[j]
            b -= tws[j]
        j -= 1
    val *= a
    act = val * val
    now = str(act)
    dow = 1
    ans = 0
    for c in now:
        x = int(c)
        ans += dow * x
        dow *= 23
        dow %= mod
        ans %= mod
    print(ans)
