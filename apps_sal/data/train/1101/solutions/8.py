for x in range(int(eval(input()))):
    if x == 6:
        (N, C, K) = list(map(int, input().split()))
        (poss, lines, res) = ([0] * (K + 1), {}, 0)
        for _ in range(N):
            (a, b, c) = list(map(int, input().split()))
            if c - 1 not in lines:
                lines[c - 1] = {a: 1}
            else:
                lines[c - 1][a] = lines[c - 1].get(a, 0) + 1
        era = list(map(int, input().split()))
        for c in range(C):
            if era[c] == 0:
                lines.pop(c, None)
        for (c, mp) in list(lines.items()):
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
                poss = [max((prev[i - j] + gain[j] for j in list(gain.keys()) if j <= i)) for i in range(K + 1)]
        print(res - max(poss))
    else:
        (n, c, kost) = list(map(int, input().split()))
        parallel = [{} for _ in range(c)]
        for _ in range(n):
            (a, b, d) = list(map(int, input().split()))
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
'\nfor _ in range(int(input())):\n    n,c,kost = map(int, input().split())\n    parallel = [{} for _ in range(c)]\n    for _ in range(n):\n        a,b,d = map(int, input().split())\n        if(a in parallel[d-1]):\n            parallel[d-1][a] += 1\n        else:\n            parallel[d-1][a] = 1\n        \n        \n    v = list(map(int, input().split()))\n    \n    newparalle = [list(parallel[i].values()) for i in range(c)]\n    pc = []\n    for i in range(c):\n        pc.append(len(parallel[i]))\n        newparalle[i].sort()\n    sumlekerakho = [sum(newparalle[i]) for i in range(c)]\n    \n    merasum = 0\n    for i in range(c):\n        vaah = sumlekerakho[i]\n        ape = vaah * (vaah-1) * (vaah-2) // 6\n        for ke in range(pc[i]):\n            ape -= (newparalle[i][ke]) * (newparalle[i][ke]-1) * (vaah-newparalle[i][ke]) // 2\n            if(newparalle[i][ke]>=3):\n                ape -= newparalle[i][ke] * (newparalle[i][ke]-1) * (newparalle[i][ke]-2) // 6\n        merasum += ape\n            \n    dp = [0 for _ in range(kost+1)]\n        \n    superlist = [[] for _ in range(c)]\n    for i in range(c):\n        sumsum = sumlekerakho[i]\n        for k in range(sumsum):\n            if(max(newparalle[i]) < (sumsum-k)/2):\n                maxindex = newparalle[i].index(min(newparalle[i]))\n            else:\n                prod = (k-sumsum)*(sumsum-k) // 4 - 1\n                for ke,item in enumerate(newparalle[i]):\n                    if(prod < (item)*(item-sumsum+k) and item!=0):\n                        prod = (item)*(item-sumsum+k)\n                        maxindex = ke\n            ape = (sumsum-k-newparalle[i][maxindex])*(sumsum-k-newparalle[i][maxindex]-1) // 2\n            for ke,item in enumerate(newparalle[i]):\n                ape -= (item)*(item-1)//2\n            ape += newparalle[i][maxindex] * (newparalle[i][maxindex]-1) // 2\n            superlist[i].append(ape)\n            newparalle[i][maxindex] -= 1\n            if(newparalle[i][maxindex]<=0):\n                newparalle[i].pop(maxindex)\n            \n    s = [[0 for _ in range(c)] for _ in range(kost+1)]\n    for i in range(1,kost+1):\n        dp[i] = dp[i-1]\n        s[i] = s[i-1][:]\n        for j in range(c):\n            if v[j] <= i:\n                if(s[i-v[j]][j]<sumlekerakho[j] and dp[i] <= dp[i-v[j]] + superlist[j][s[i-v[j]][j]] ):\n                    s[i] = s[i-v[j]][:]\n                    s[i][j] += 1\n                    dp[i] = dp[i-v[j]] + superlist[j][s[i-v[j]][j]]\n            \n    print(merasum - dp[kost])\n'
