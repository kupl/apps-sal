import sys

sys.setrecursionlimit(10 ** 5)
def int1(x): return int(x) - 1
def p2D(x): return print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def MI1(): return map(int1, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]


for _ in range(II()):
    n, k = MI()
    to = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = MI1()
        to[u].append(v)
        to[v].append(u)

    if k == 1:
        print(n - 1)
        continue

    dp = [0] * n
    beleaf = [False] * n
    leaves = [0] * n
    stack = [(0, -1)]
    first = [True] * n
    while stack:
        u, pu = stack.pop()
        if first[u]:
            first[u] = False
            stack.append((u, pu))
            for v in to[u]:
                if v == pu:
                    continue
                stack.append((v, u))
        else:
            dp[u] = leaves[u] // k
            if pu != -1 and dp[u] * k + 1 == len(to[u]):
                leaves[pu] += 1
                beleaf[u] = True
            for v in to[u]:
                if v == pu:
                    continue
                dp[u] += dp[v]
    """
    print(dp)
    print(leaves)
    print(beleaf)
    """

    stack = [(0, -1)]
    while stack:
        u, pu = stack.pop()
        for v in to[u]:
            if v == pu:
                continue
            dp[v] = dp[u]
            if (leaves[u] - beleaf[v]) % k == 0 and (leaves[u] - beleaf[v]) + 1 == len(to[u]):
                leaves[v] += 1
                if leaves[v] % k == 0:
                    dp[v] += 1
            stack.append((v, u))
    """
    print(dp)
    print(leaves)
    print(beleaf)
    """
    print(max(dp))
