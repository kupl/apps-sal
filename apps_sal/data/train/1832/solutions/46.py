import heapq


class Solution:
    def reachableNodes(self, edges: List[List[int]], M: int, N: int) -> int:
        graph = collections.defaultdict(dict)
        for u, v, cost in edges:
            graph[u][v] = graph[v][u] = cost
        
        # Dijkstra
        pq = [(-M, 0)]
        seen = {}
        while pq:
            moves, i = heapq.heappop(pq)
            if i not in seen:
                seen[i] = -moves
                for j in graph[i]:
                    rem_moves = -moves - graph[i][j] - 1
                    if j not in seen and rem_moves >= 0:
                        heapq.heappush(pq, (-rem_moves, j))
        res = len(seen) # Reachable big nodes
        for i, j, cost in edges:
            res += min(seen.get(i, 0) + seen.get(j, 0), cost)
        return res
