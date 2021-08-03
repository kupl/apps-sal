import math

dp = []
dp.append(0)
for i in range(1, 1000005):
    dp.append(math.log(i) + dp[i - 1])

t = int(input())
for i in range(t):
    n, m, p, k = input().split()
    n = int(n)
    m = int(m)
    p = int(p)
    k = int(k)

    if p == 0 or (n % 2 == 0 and m % 2 == 0):
        ans = 1.0
        print(ans)
    elif n % 2 == 1 and m % 2 == 1:
        ans = 0.0
        print(ans * 100)
    else:
        P = 0
        kln2 = k * math.log(2)
        for i in range(p, k + 1):
            lnPi = dp[k] - dp[i] - dp[k - i] - kln2
            Pi = pow(math.e, lnPi)
            P += Pi
        print(P)
