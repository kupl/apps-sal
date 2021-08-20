import sys
sys.setrecursionlimit(1000000)
t = int(input())
for _ in range(t):
    (n, q) = map(int, input().split())
    par = [i for i in range(2 * n)]

    def get(u):
        if u != par[u]:
            par[u] = get(par[u])
        return par[u]

    def union(u, v):
        par[get(u)] = get(v)
    for i in range(q):
        (i, j, val) = map(int, input().split())
        i -= 1
        j -= 1
        if val == 0:
            union(i, j)
            union(i + n, j + n)
        else:
            union(i, j + n)
            union(i + n, j)
    if any((get(i) == get(i + n) for i in range(n))):
        print('no')
    else:
        print('yes')
