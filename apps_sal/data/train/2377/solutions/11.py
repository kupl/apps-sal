t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    p = []
    for i in range(n):
        p.append((a[i],i))
    p.sort(key = lambda x: x[0])
    aOrder = [-1] * n
    for i in range(n):
        aOrder[p[i][1]] = i
    maxSubseq = []
    for i in range(n):
        maxSubseqcur = 0
        for j in range(i):
            if aOrder[i] - aOrder[j] == 1 and maxSubseqcur < maxSubseq[j]:
                maxSubseqcur = maxSubseq[j]
        maxSubseq.append(maxSubseqcur + 1)
    print(n - max(maxSubseq))
