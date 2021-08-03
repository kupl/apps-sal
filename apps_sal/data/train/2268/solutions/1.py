mod = 1000000007
eps = 10**-9


def main():
    import sys
    from collections import deque
    input = sys.stdin.readline

    N = int(input())
    P = list(map(int, input().split()))
    adj = [[] for _ in range(N + 1)]
    adj_directed = [[] for _ in range(N + 1)]
    adj_rev = [[] for _ in range(N + 1)]
    out = [0] * (N + 1)
    for i, p in enumerate(P):
        adj_directed[p].append(i + 1)
        adj[p].append(i + 1)
        adj[i + 1].append(p)
        adj_rev[i + 1].append(p)
        out[p] += 1

    que = deque()
    que.append(1)
    seen = [-1] * (N + 1)
    seen[1] = 0
    par = [-1] * (N + 1)
    back_from = -1
    back_to = -1
    while que:
        v = que.popleft()
        for u in adj[v]:
            if seen[u] == -1:
                seen[u] = seen[v] + 1
                que.append(u)
                par[u] = v
            else:
                if par[v] != u:
                    if P[v - 1] == u:
                        back_from = u
                        back_to = v
                        out[u] -= 1

    G = [-1] * (N + 1)
    for v in range(1, N + 1):
        if out[v] == 0:
            que.append(v)
    while que:
        v = que.popleft()
        M = set()
        for u in adj_directed[v]:
            if v == back_from and u == back_to:
                continue
            M.add(G[u])
        for i in range(N + 1):
            if i not in M:
                G[v] = i
                break
        for u in adj_rev[v]:
            if v == back_to and u == back_from:
                continue
            out[u] -= 1
            if out[u] == 0:
                que.append(u)

    if G[back_from] != G[back_to]:
        print("POSSIBLE")
        return

    cycle = set()
    v = back_from
    while v > 0:
        cycle.add(v)
        v = par[v]
    v = back_to
    while v > 0:
        cycle.add(v)
        v = par[v]

    v = back_from
    seen = {v}
    while True:
        M = set()
        for u in adj_directed[v]:
            M.add(G[u])
        for i in range(N + 1):
            if i not in M:
                if G[v] == i:
                    print("POSSIBLE")
                    return
                G[v] = i
                break
        fin = 1
        for u in adj_rev[v]:
            if u in cycle and u not in seen:
                v = u
                seen.add(u)
                fin = 0
                break
        if fin:
            break
    print("IMPOSSIBLE")


def __starting_point():
    main()


__starting_point()
