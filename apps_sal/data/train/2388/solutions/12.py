from collections import deque
import sys


def __starting_point():
    t = int(input())
    lns = sys.stdin.readlines()
    i = 0
    result = []
    for _ in range(t):
        n, m = map(int, lns[i].split())
        i += 1
        g = [[] for _ in range(n)]
        for _ in range(m):
            v, u = map(int, lns[i].split())
            i += 1
            g[v - 1].append(u - 1)
            g[u - 1].append(v - 1)

        q = deque()
        vis = [False] * n
        lvl = [-1] * n
        lvl[0] = 0
        vis[0] = True
        q.append(0)
        while len(q) > 0:
            v = q.popleft()
            for u in g[v]:
                if not vis[u]:
                    vis[u] = True
                    lvl[u] = lvl[v] + 1
                    q.append(u)

        odd = [str(i + 1) for i in range(n) if lvl[i] % 2 == 1]
        even = [str(i + 1) for i in range(n) if lvl[i] % 2 == 0]
        res = odd if len(odd) < len(even) else even
        result.append(str(len(res)))
        result.append(" ".join(res))

    print("\n".join(result))


__starting_point()
