from sys import stdin, setrecursionlimit
from collections import deque
input = stdin.readline
def getstr(): return input()[:-1]
def getint(): return int(input())
def getints(): return list(map(int, input().split()))
def getint1(): return list([int(x) - 1 for x in input().split()])

adj = col = comp = []
cnt0 = cnt1 = 0

def dfs(us, cs, cmp, n):
    nonlocal adj, col, comp, cnt0, cnt1
    stack = [(us, cs)]
    inq = [False] * n
    inq[us] = True
    while len(stack) > 0:
        u, c = stack.pop()
        # print(u, c)
        inq[u] = False
        col[u] = c
        if col[u] == 0: cnt0 += 1
        else: cnt1 += 1
        comp[u] = cmp
        for v, ch in adj[u]:
            if col[v] == -1 and not inq[v]:
                inq[v] = True
                stack.append((v, c ^ ch))
    # print(col, comp)

def solve():
    nonlocal adj, col, comp, cnt0, cnt1
    n = getint()
    a = []
    pos = [[] for _ in range(n)]
    adj = [[] for _ in range(n)]
    for i in [0, 1]:
        a.append(getint1())
        for j, x in enumerate(a[i]):
            pos[x].append(j)
    for i, c in enumerate(pos):
        if len(c) != 2:
            print("-1")
            return
        if c[0] == c[1]: 
            continue
        r1 = int(a[0][c[0]] != i)
        r2 = int(a[0][c[1]] != i)
        adj[c[0]].append((c[1], int(r1 == r2)))
        adj[c[1]].append((c[0], int(r1 == r2)))
    # print(adj)
    col = [-1] * n
    comp = [-1] * n
    colcnt = []
    ans = cnt = 0
    # cnt = 0
    for i in range(n):
        if col[i] == -1:
            cnt0, cnt1 = 0, 0
            dfs(i, 0, cnt, n)
            cnt += 1
            colcnt.append((cnt0, cnt1))
            ans += min(cnt0, cnt1)
    # print(colcnt)

    print(ans)
    alist = []
    for i in range(n):
        chz = int(colcnt[comp[i]][0] < colcnt[comp[i]][1])
        if col[i] ^ chz:
            alist.append(i + 1)
    # print(len(alist))
    print(*alist)

def __starting_point():
    # solve()
    # for t in range(getint()):
    #     print("Case #{}: ".format(t + 1), end="")
    #     solve()
    for _ in range(getint()):
        solve()

__starting_point()
