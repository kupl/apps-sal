t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    p = []
    for i in range(n):
        p.append((a[i],i))
    p.sort(key = lambda x: x[0])
    aOrder = [-1] * n
    curIndex = 0
    for i in range(n):
        if i >= 1 and p[i][0] != p[i-1][0]:
            curIndex += 1
        aOrder[p[i][1]] = curIndex
    aCount = [0] * (curIndex + 1)
    for i in range(n):
        aCount[aOrder[i]] += 1
    maxSubseq0 = [0] * (curIndex + 1) # Only using one number
    maxSubseq1 = [0] * (curIndex + 1) # Extendable to next number but using >=2 numbers
    maxSubseq2 = [0] * (curIndex + 1) # How many current number is there in maxSubseq1 sequence
    maxSubseq3 = [0] * (curIndex + 1) # Not extendable to next number (not necessarily counted if < maxSubseq1)
    for i in range(n):
        aCurOrder = aOrder[i]
        curSubseq1 = maxSubseq1[aCurOrder] + 1
        curSubseq2 = maxSubseq2[aCurOrder] + 1
        curSubseq3 = maxSubseq3[aCurOrder] + 1
        if curSubseq1 == 1:
            curSubseq1 = 0
            curSubseq2 = 0
        if curSubseq3 == 1:
            curSubseq3 = 0
        maxSubseq0[aCurOrder] += 1
        justUpdated = False
        if aCurOrder >= 1 and maxSubseq0[aCurOrder - 1] > 0:
            if curSubseq1 == 0:
                curSubseq1 = maxSubseq0[aCurOrder - 1] + 1
                curSubseq2 = 1
                justUpdated = True
            elif  curSubseq1 < maxSubseq0[aCurOrder - 1] + 1 and curSubseq3 < maxSubseq0[aCurOrder - 1] + 1:
                curSubseq3 = maxSubseq0[aCurOrder - 1] + 1
        if aCurOrder >= 1 and maxSubseq1[aCurOrder - 1] > 0 and maxSubseq2[aCurOrder - 1] == aCount[aCurOrder - 1]:
            if curSubseq1 == 0 or justUpdated:
                curSubseq1 = maxSubseq1[aCurOrder - 1] + 1
                curSubseq2 = 1
            elif  curSubseq1 < maxSubseq1[aCurOrder - 1] + 1 and curSubseq3 < maxSubseq1[aCurOrder - 1] + 1:
                curSubseq3 = maxSubseq1[aCurOrder - 1] + 1
        maxSubseq1[aCurOrder] = curSubseq1
        maxSubseq2[aCurOrder] = curSubseq2
        maxSubseq3[aCurOrder] = curSubseq3

    print(n - max(maxSubseq0 + maxSubseq1 + maxSubseq3))
