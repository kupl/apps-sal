def main():
    import sys
    sys.setrecursionlimit(100000)
    input = sys.stdin.readline
    from heapq import heappop, heappush
    mod = 10**9 + 7
    INF = 1 << 60
    N, M = list(map(int, input().split()))
    S, T = list(map(int, input().split()))
    E = [[] for _ in range(N + 1)]
    edges = []
    for u, v, d in zip(*[iter(map(int, sys.stdin.read().split()))] * 3):
        E[u].append((v, d))
        E[v].append((u, d))
        edges.append((u, v, d))

    def dijksrtra(start):
        Dist = [INF] * (N + 1)
        Dist[start] = 0
        q = [0 << 17 | start]
        mask = (1 << 17) - 1
        while q:
            dist_v = heappop(q)
            v = dist_v & mask
            dist = dist_v >> 17
            if Dist[v] != dist:
                continue
            for u, d in E[v]:
                new_dist = dist + d
                if Dist[u] > new_dist:
                    Dist[u] = new_dist
                    heappush(q, new_dist << 17 | u)
        return Dist

    Dist_S = dijksrtra(S)
    Dist_T = dijksrtra(T)
    dist_st = Dist_S[T]

    DAG_edges = []
    DAG = [[] for _ in range(N + 1)]
    DAG_rev = [[] for _ in range(N + 1)]
    for u, v, d in edges:
        if Dist_S[u] + Dist_T[v] + d == dist_st:
            DAG_edges.append((u, v))
            DAG[u].append(v)
            DAG_rev[v].append(u)
        elif Dist_T[u] + Dist_S[v] + d == dist_st:
            DAG_edges.append((v, u))
            DAG[v].append(u)
            DAG_rev[u].append(v)

    V = []
    rem = [0] * (N + 1)
    for _, v in DAG_edges:
        rem[v] += 1
    q = [S]
    while q:
        v = q.pop()
        V.append(v)
        for u in DAG[v]:
            rem[u] -= 1
            if rem[u] == 0:
                q.append(u)

    n_paths_S = [0] * (N + 1)
    n_paths_T = [0] * (N + 1)
    n_paths_S[S] = 1
    n_paths_T[T] = 1

    for v in V:
        n = n_paths_S[v]
        for u in DAG[v]:
            n_paths_S[u] += n
    for v in V[::-1]:
        n = n_paths_T[v]
        for u in DAG_rev[v]:
            n_paths_T[u] += n
    ans = n_paths_S[T]
    ans = ans * ans % mod

    for v, u in DAG_edges:
        if Dist_S[v] * 2 < dist_st and dist_st < Dist_S[u] * 2:
            ans = (ans - (n_paths_S[v] * n_paths_T[u])**2) % mod

    for v, (dist, ns, nt) in enumerate(zip(Dist_S, n_paths_S, n_paths_T)):
        if dist * 2 == dist_st:
            ans = (ans - (ns * nt)**2) % mod

    print(ans)


main()
