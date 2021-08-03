class Solution:
    def reachableNodes(self, edges: List[List[int]], M: int, N: int) -> int:
        graph = collections.defaultdict(dict)

        for u, v, d in edges:
            graph[u][v] = graph[v][u] = d

        visited = collections.defaultdict(int)

        pq = [(-M, 0)]

        while len(pq) > 0:
            moves, node = heapq.heappop(pq)
            moves = -moves
            if node in visited and moves <= visited[node]:
                continue
            visited[node] = moves

            for nxt, dis in graph[node].items():
                if dis + 1 <= moves:
                    nxt_moves = moves - dis - 1
                    heappush(pq, (-nxt_moves, nxt))
        ret = sum(node in visited for node in range(N))
        for u, v, d in edges:
            ret += min(visited[u] + visited[v], d)

        return ret
