def insort(l, v):
    s = 0
    e = len(l)
    while True:
        mid = (s + e) // 2
        if s == e or mid > len(l):
            break
        if l[mid][0] < v[0]:
            s = mid + 1
        elif l[mid][0] > v[0]:
            e = mid
        else:
            break
    l.insert(mid, v)


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
        pq_l = [[] for _ in range(l)]
        for i in range(1, n):
            il = 1
            dif_l = []
            for j in range(i):
                dif = abs(i_l[i][1] - i_l[j][1])
                dif_l.append(dif)
                dp[i][il] = max(dp[i][il], dif)
            for il in range(2, min(l, i + 1)):
                for (prev_max, ind) in reversed(pq_l[il - 1]):
                    if ind == i:
                        continue
                    if prev_max < dp[i][il]:
                        break
                    else:
                        dp[i][il] = max(dp[i][il], min(dif_l[ind], prev_max))
                insort(pq_l[il], [dp[i][il], i])
            il = 1
            insort(pq_l[il], [dp[i][il], i])
            ans = max(ans, dp[i][-1])
    print(ans)
