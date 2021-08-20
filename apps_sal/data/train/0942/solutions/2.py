for _ in range(int(input())):
    (n, l) = map(int, input().split())
    a_l = list(map(int, input().split()))
    dic = {}
    dif = 0
    for (i, v) in enumerate(a_l, start=1):
        if v not in dic:
            dic[v] = [i, i]
        else:
            dic[v][0] = min(dic[v][0], i)
            dic[v][1] = max(dic[v][1], i)
            dif = max(dif, dic[v][1] - dic[v][0])
    ans = dif
    if l <= len(set(a_l)):
        i_l = [[v, i] for (i, v) in enumerate(a_l, start=1)]
        i_l.sort(reverse=True)
        dp = [[-1 for _ in range(l)] for _ in range(n)]
        for i in range(1, n):
            for j in range(i):
                dif = abs(i_l[i][1] - i_l[j][1])
                dp[i][1] = max(dp[i][1], dif)
                for il in range(2, l):
                    if dp[j][il - 1] == -1:
                        break
                    dp[i][il] = max(dp[i][il], min(dif, dp[j][il - 1]))
            ans = max(ans, dp[i][il])
    print(ans)
