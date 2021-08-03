for _ in range(int(input())):
    n = int(input())
    con = list(map(int, input().split()))
    le = [1 for i in range(n)]
    for i in range(n - 2, -1, -1):
        le[con[i] - 1] += le[i + 1]
    ans = [0 for i in range(n)]
    ma = 0
    tra = [[] for i in range(n + 1)]
    no = 2
    for i in con:
        tra[i].append(no)
        no += 1
    bfs = [1]
    l = 0
    while l < len(bfs):
        go = bfs[l]
        for i in tra[go]:
            bfs.append(i)
        l += 1
    ans[0] = le[0]
    for i in range(1, n, 1):
        ci = bfs[i]
        va = le[ci - 1] + ans[con[ci - 2] - 1]
        if va > ma:
            ma = va
        ans[ci - 1] = va
    print(ma)
