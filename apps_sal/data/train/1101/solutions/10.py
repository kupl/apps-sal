for x in range(int(input())):
    if x == 6:
        (n, c, kost) = map(int, input().split())
        parallel = [{} for _ in range(c)]
        for _ in range(n):
            (a, b, d) = map(int, input().split())
            if a in parallel[d - 1]:
                parallel[d - 1][a] += 1
            else:
                parallel[d - 1][a] = 1
        v = list(map(int, input().split()))
        newparalle = [list(parallel[i].values()) for i in range(c)]
        pc = []
        for i in range(c):
            pc.append(len(parallel[i]))
            newparalle[i].sort()
        sumlekerakho = [sum(newparalle[i]) for i in range(c)]
        merasum = 0
        for i in range(c):
            vaah = sumlekerakho[i]
            ape = vaah * (vaah - 1) * (vaah - 2) // 6
            for ke in range(pc[i]):
                ape -= newparalle[i][ke] * (newparalle[i][ke] - 1) * (vaah - newparalle[i][ke]) // 2
                if newparalle[i][ke] >= 3:
                    ape -= newparalle[i][ke] * (newparalle[i][ke] - 1) * (newparalle[i][ke] - 2) // 6
            merasum += ape
        dp = [0 for _ in range(kost + 1)]
        superlist = [[] for _ in range(c)]
        for i in range(c):
            sumsum = sumlekerakho[i]
            for k in range(sumsum):
                if max(newparalle[i]) < (sumsum - k) / 2:
                    maxindex = newparalle[i].index(min(newparalle[i]))
                else:
                    prod = (k - sumsum) * (sumsum - k) // 4 - 1
                    for (ke, item) in enumerate(newparalle[i]):
                        if prod < item * (item - sumsum + k) and item != 0:
                            prod = item * (item - sumsum + k)
                            maxindex = ke
                ape = (sumsum - k - newparalle[i][maxindex]) * (sumsum - k - newparalle[i][maxindex] - 1) // 2
                for (ke, item) in enumerate(newparalle[i]):
                    ape -= item * (item - 1) // 2
                ape += newparalle[i][maxindex] * (newparalle[i][maxindex] - 1) // 2
                superlist[i].append(ape)
                newparalle[i][maxindex] -= 1
                if newparalle[i][maxindex] <= 0:
                    newparalle[i].pop(maxindex)
        s = [[0 for _ in range(c)] for _ in range(kost + 1)]
        for i in range(1, kost + 1):
            dp[i] = dp[i - 1]
            s[i] = s[i - 1][:]
            for j in range(c):
                if v[j] <= i:
                    if s[i - v[j]][j] < sumlekerakho[j] and dp[i] <= dp[i - v[j]] + superlist[j][s[i - v[j]][j]]:
                        s[i] = s[i - v[j]][:]
                        s[i][j] += 1
                        dp[i] = dp[i - v[j]] + superlist[j][s[i - v[j]][j]]
        print(merasum - dp[kost])
    else:
        (N, C, K) = map(int, input().split())
        (poss, lines, res) = ([0] * (K + 1), {}, 0)
        for _ in range(N):
            (a, b, c) = map(int, input().split())
            if c - 1 not in lines:
                lines[c - 1] = {a: 1}
            else:
                lines[c - 1][a] = lines[c - 1].get(a, 0) + 1
        era = list(map(int, input().split()))
        for c in range(C):
            if era[c] == 0:
                lines.pop(c, None)
        for (c, mp) in lines.items():
            vals = list(mp.values())
            if len(vals) >= 3:
                vals.sort()
                (s1, s2, s3) = (sum(vals), sum((a ** 2 for a in vals)), sum((a ** 3 for a in vals)))
                full = (s1 ** 3 - 3 * s1 * s2 + 2 * s3) // 6
                res += full
                gain = {0: 0}
                idx = 0
                for j in range(era[c], K + 1, era[c]):
                    vals[idx] -= 1
                    old = vals[idx] + 1
                    nw = vals[idx]
                    if vals[idx] == 0:
                        idx += 1
                        if idx == len(vals):
                            break
                    s1 -= 1
                    s2 += nw ** 2 - old ** 2
                    s3 += nw ** 3 - old ** 3
                    gain[j] = full - (s1 ** 3 - 3 * s1 * s2 + 2 * s3) // 6
                prev = poss
                poss = [max((prev[i - j] + gain[j] for j in gain.keys() if j <= i)) for i in range(K + 1)]
        print(res - max(poss))
