def main():
    import sys
    from collections import deque, defaultdict
    from heapq import heappop, heappush
    sys.setrecursionlimit(10 ** 9)
    input = sys.stdin.readline
    for __ in [0] * int(input()):
        (N, M) = list(map(int, input().split()))
        deg = [0] * N
        directed = defaultdict(list)
        undirected = defaultdict(list)
        for _ in [0] * M:
            (t, a, b) = list(map(int, input().split()))
            a -= 1
            b -= 1
            if t:
                directed[a].append(b)
                deg[b] += 1
            else:
                undirected[a].append(b)
                undirected[b].append(a)
        q = deque([i for (i, d) in enumerate(deg) if d == 0])
        topological = []
        while q:
            v = q.popleft()
            topological.append(v)
            if v not in directed:
                continue
            for u in directed[v]:
                deg[u] -= 1
                if deg[u] == 0:
                    q.append(u)
        if len(topological) != N:
            print('NO')
            continue
        del deg
        print('YES')
        used = [0] * N
        for v in topological:
            if v in directed:
                for u in directed[v]:
                    print(v + 1, u + 1)
            if v in undirected:
                for u in undirected[v]:
                    if used[u]:
                        continue
                    print(v + 1, u + 1)
            used[v] = 1
        del used


def __starting_point():
    main()


__starting_point()
