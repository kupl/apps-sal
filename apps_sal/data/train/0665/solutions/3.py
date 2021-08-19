for _ in range(int(input())):
    (n, m) = list(map(int, input().split()))
    r = list(map(int, input().split()))
    mat = [[] for i in range(n)]
    ranking = [[] for i in range(n)]
    for i in range(n):
        l = list(map(int, input().split()))
        cur = r[i]
        for j in l:
            cur += j
            mat[i].append(cur)
    for i in range(m):
        ar = []
        for j in range(n):
            ar.append([mat[j][i], j])
        ar.sort(reverse=True, key=lambda x: x[0])
        prev = -1
        r = 1
        x = 1
        for j in range(n):
            if ar[j][0] != prev:
                r = x
            ranking[ar[j][1]].append(r)
            prev = ar[j][0]
            x += 1
    brt = []
    brk = []
    for i in range(n):
        brt.append(mat[i].index(max(mat[i])))
    for i in range(n):
        brk.append(ranking[i].index(min(ranking[i])))
    ans = 0
    for i in range(n):
        if brk[i] != brt[i]:
            ans += 1
    print(ans)
