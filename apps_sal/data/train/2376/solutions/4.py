def main():
    from heapq import heapify, heappop, heappush
    import sys
    input = sys.stdin.readline
    for __ in [0]*int(input()):
        N, K = list(map(int, input().split()))

        G = [[] for _ in [0]*N]
        deg = [0]*N
        for _ in [0]*(N-1):
            a, b = list(map(int, input().split()))
            a -= 1
            b -= 1
            G[a].append(b)
            G[b].append(a)
            deg[a] += 1
            deg[b] += 1

        if K == 1:
            print(N-1)
            continue

        leaf = [0]*N

        for v in range(N):
            if deg[v] == 1:
                u = G[v][0]
                leaf[u] += 1

        L = [(-l, v) for v, l in enumerate(leaf) if l >= K]
        heapify(L)

        ans = 0
        while L:
            l, v = heappop(L)
            if -l != leaf[v]:
                continue
            q, r = divmod(-l, K)
            ans += q
            leaf[v] = r
            deg[v] -= K*q

            p = -1
            cnt = 0
            for u in G[v]:
                if deg[u] == 1 and cnt < K*q:
                    cnt += 1
                    deg[u] = 0
                elif deg[u]:
                    p = u
                if cnt == K*q and (deg[v] != 1 or p != -1):
                    break

            if deg[v] == 1:
                if p != -1:
                    leaf[p] += 1
                    if leaf[p] >= K:
                        heappush(L, (-leaf[p], p))
        print(ans)


def __starting_point():
    main()

__starting_point()
