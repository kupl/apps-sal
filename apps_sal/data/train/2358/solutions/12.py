def resolve():
    import sys
    input = sys.stdin.readline
    import heapq

    def dijkstra_heap(s, g, edge):
        d = [10 ** 20] * (n + 2)
        used = [True] * (n + 2)
        d[s] = 0
        used[s] = False
        edgelist = []
        (sx, sy, sr) = (edge[s][0], edge[s][1], edge[s][2])
        for i in range(n + 2):
            (x, y, r) = (edge[i][0], edge[i][1], edge[i][2])
            dist = ((x - sx) ** 2 + (y - sy) ** 2) ** (1 / 2)
            heapq.heappush(edgelist, (max(dist - r - sr, 0), i))
        while len(edgelist):
            minedge = heapq.heappop(edgelist)
            v = minedge[1]
            if not used[v]:
                continue
            d[v] = minedge[0]
            used[v] = False
            (bx, by, br) = (edge[v][0], edge[v][1], edge[v][2])
            for i in range(n + 2):
                (x, y, r) = (edge[i][0], edge[i][1], edge[i][2])
                dist = ((x - bx) ** 2 + (y - by) ** 2) ** (1 / 2)
                if used[i]:
                    heapq.heappush(edgelist, (max(dist - r - br, 0) + d[v], i))
            if not used[g]:
                break
        return d[g]
    (sx, sy, gx, gy) = map(int, input().split())
    n = int(input())
    edge = [(sx, sy, 0), (gx, gy, 0)]
    for i in range(2, n + 2):
        (x, y, r) = map(int, input().split())
        edge.append((x, y, r))
    print(dijkstra_heap(0, 1, edge))


def __starting_point():
    resolve()


__starting_point()
