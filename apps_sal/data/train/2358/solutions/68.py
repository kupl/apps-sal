import sys
import heapq
my_input = sys.stdin.readline


def main():
    (xs, ys, xt, yt) = list(map(int, my_input().split()))
    N = int(my_input())
    C = [(xs, ys, 0), (xt, yt, 0)]
    C += [tuple(map(int, my_input().split())) for i in range(N)]
    G = [[] for i in range(N + 2)]
    for i in range(N + 2):
        for j in range(i + 1, N + 2):
            cost = max(0, ((C[i][0] - C[j][0]) ** 2 + (C[i][1] - C[j][1]) ** 2) ** 0.5 - (C[i][2] + C[j][2]))
            G[i].append((j, cost))
            G[j].append((i, cost))

    def dijkstra(graph, start, inf=float('inf')):
        import heapq
        n = len(graph)
        distances = [inf] * n
        distances[start] = 0
        visited = [False] * n
        hq = [(0, start)]
        while hq:
            (dist, fr) = heapq.heappop(hq)
            if distances[fr] < dist:
                continue
            if fr == 1:
                return distances
            visited[fr] = True
            for (to, cost) in graph[fr]:
                new_dist = distances[fr] + cost
                if visited[to] or distances[to] <= new_dist:
                    continue
                distances[to] = new_dist
                heapq.heappush(hq, (new_dist, to))
        return distances
    dist = dijkstra(G, 0)
    print(dist[1])


def __starting_point():
    main()


__starting_point()
