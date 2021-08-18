import sys
from collections import defaultdict
t = int(input())

for _ in range(t):
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    adj = []
    for _ in range(n):
        x = list(map(int, input().split()))
        adj.append(x)

    rating = defaultdict(lambda: -1)

    rank = [[-1 for i in range(m + 1)]for j in range(n)]

    b = [[-1 for i in range(m + 1)]for j in range(n)]
    for i in range(n):
        b[i][0] = a[i]
    for i in range(0, n):
        for j in range(1, m + 1):
            b[i][j] = b[i][j - 1] + adj[i][j - 1]

    for j in range(1, m + 1):
        g = []
        d = {}
        for i in range(n):
            g.append(b[i][j])
        z = sorted(g, reverse=True)
        c = 0
        for i in z:
            if(i not in d):
                c += 1
                d[i] = c
            else:
                c += 1
        for i in range(n):
            rank[i][j] = d[b[i][j]]

    for i in range(n):
        mx = -1
        for x in range(1, m + 1):
            mx = max(mx, b[i][x])
        for j in range(1, m + 1):
            if(b[i][j] == mx):
                rating[i] = j
                break
    c = 0
    '''for i in b:
     print(*i)
    print()
    for i in rank:
     print(*i)'''

    for i in range(n):
        ans = []
        mi = sys.maxsize
        for x in range(1, m + 1):
            mi = min(mi, rank[i][x])
        for j in range(1, m + 1):
            if(rank[i][j] == mi):
                if(j != rating[i]):
                    c += 1
                break

    print(c)
