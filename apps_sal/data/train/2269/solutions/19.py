import sys
def input(): return sys.stdin.readline().rstrip()


sys.setrecursionlimit(max(1000, 10**9))
def write(x): return sys.stdout.write(x + "\n")


n, m = list(map(int, input().split()))
mt = [[True] * n for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    mt[a][b] = False
    mt[b][a] = False
for i in range(n):
    mt[i][i] = False
ns = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if mt[i][j]:
            ns[i].append(j)


def is_bip(ns):
    cs = [None] * n
    vs = []
    for start in range(n):
        if cs[start] is not None:
            continue
        v0 = v1 = 0
        q = [start]
        cs[start] = 1
        v1 += 1
        while q:
            u = q.pop()
            c = cs[u]
            cc = int(not c)
            for v in ns[u]:
                if cs[v] is None:
                    cs[v] = cc
                    if cc == 0:
                        v0 += 1
                    else:
                        v1 += 1
                    q.append(v)
                elif cs[v] == c:
                    return False, None
        vs.append((v0, v1))
    return True, vs


res, vs = is_bip(ns)
if not res:
    ans = -1
else:
    dp = 1
    for v0, v1 in vs:
        dp = (dp << v0) | (dp << v1)
    ans = float("inf")
    for i in range(1, n + 1):
        if dp >> i & 1:
            ans = min(ans, i * (i - 1) // 2 + (n - i) * (n - i - 1) // 2)
print(ans)
