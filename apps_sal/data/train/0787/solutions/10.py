t = int(input())
for _ in range(t):
    s = input()
    pre = []
    n = len(s)
    j = 0
    ss = {}
    for i in range(n):
        if s[i] == "1":
            pre.append(i)
            ss[i] = j
            j += 1
    pre.append(n)
    suff = [0 for i in range(n + 1)]
    tot = 0
    duff = [0 for i in range(n + 1)]
    for i in range(n - 1, -1, -1):
        if s[i] == "0":
            pass
        else:

            suff[i] = suff[pre[ss[i] + 1]] + max(tot, 0)
            duff[i] = max(tot, 0)
            tot -= 1
        tot += 1
    tot = 0
    st = False
    dp = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        if s[i] == "0":
            st = True
            continue
        else:
            if st:
                tot += 1
                st = False
            dp[i] = tot + dp[pre[ss[i] + 1]]

    print(suff[pre[0]] + dp[pre[0]])
