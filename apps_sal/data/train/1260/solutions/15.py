# cook your dish here
import sys
t = int(input())
sys.setrecursionlimit(1000000)


def dfs(node):
    nonlocal l, vis
    st = True
    for i in adj[node]:
        if i in l:
            vis[a] += it[i]
            st = False
            l.remove(i)
            #print('visited here',vis)
            #print('L here',l)
            dfs(i)
    if st:
        return ''


for _ in range(t):
    n, m, k = list(map(int, input().split()))
    adj = [[] for i in range(n)]
    l = set(range(0, n))
    # print('l',l)
    for i in range(m):
        x, y = list(map(int, input().split()))
        adj[x - 1].append(y - 1)
        adj[y - 1].append(x - 1)
    # print('graph',adj)
    it = list(map(int, input().split()))
    # print('it',it)
    vis = {}
    cost = []
    while l != set():
        a = l.pop()
        # print('a',a)
        vis[a] = it[a]
        dfs(a)
        cost.append(vis[a])
        # print('cost',cost)
    cost.sort()
    if len(cost) < k:
        print(-1)
        continue
    mi = 0
    ma = len(cost)
    su = 0
    for i in range(k):
        if i % 2 == 0:
            # print('EVEN','i',i,'ma-1',ma-1,'cost[ma-1]',cost[ma-1])
            su += cost[ma - 1]
            ma -= 1
        else:
            # print('ODD','i',i,'mi',mi,'cost[mi]',cost[mi])
            su += cost[mi]
            mi += 1
    print(su)
