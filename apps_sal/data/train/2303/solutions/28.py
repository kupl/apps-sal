def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    (N, M) = list(map(int, input().split()))
    adj = [[] for _ in range(N + 1)]
    c2v = {}
    v = N + 1
    for _ in range(M):
        (p, q, c) = list(map(int, input().split()))
        P = p * 10 ** 7 + c
        Q = q * 10 ** 7 + c
        if P not in c2v:
            c2v[P] = v
            adj[p].append((v, 1))
            adj.append([(p, 1)])
            v += 1
        if Q not in c2v:
            c2v[Q] = v
            adj[q].append((v, 1))
            adj.append([(q, 1)])
            v += 1
        adj[c2v[P]].append((c2v[Q], 0))
        adj[c2v[Q]].append((c2v[P], 0))
    que = deque()
    que.append(1)
    seen = [-1] * len(adj)
    seen[1] = 0
    while que:
        v = que.popleft()
        for (u, cost) in adj[v]:
            if seen[u] == -1:
                seen[u] = seen[v] + cost
                if cost:
                    que.append(u)
                else:
                    que.appendleft(u)
    print(seen[N] // 2)


def __starting_point():
    main()


__starting_point()
