t = int(input())
for you in range(t):
    n = int(input())
    l = input().split()
    li = [int(i) for i in l]
    z = list(li)
    z.sort()
    hashi = dict()
    for i in range(n):
        hashi[z[i]] = i + 1
    for i in range(n):
        li[i] = hashi[li[i]]
    hashi = dict()
    dp = [0 for i in range(n)]
    for i in range(n):
        if li[i] - 1 in hashi:
            dp[i] = hashi[li[i] - 1] + 1
            hashi[li[i]] = dp[i]
        else:
            dp[i] = 1
            hashi[li[i]] = 1
    z = max(dp)
    print(n - z)
