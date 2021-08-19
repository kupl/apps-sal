class Solution:

    def reachableNodes(self, edges: List[List[int]], M: int, N: int) -> int:
        graph = [[] for _ in range(N)]
        remain = [[0] * N for _ in range(N)]
        for edge in edges:
            (i, j, t) = edge
            graph[i].append((j, t))
            graph[j].append((i, t))
            remain[i][j] = remain[j][i] = t
        pq = [(0, 0)]
        seen = set()
        res = 0
        while pq:
            (dist, node) = heapq.heappop(pq)
            if node in seen:
                continue
            res += 1
            seen.add(node)
            for (nei, d) in graph[node]:
                valid = min(M - dist, remain[node][nei])
                res += valid
                remain[node][nei] = remain[nei][node] = remain[nei][node] - valid
                cost_to_nei = dist + d + 1
                if cost_to_nei <= M and nei not in seen:
                    heapq.heappush(pq, (cost_to_nei, nei))
        return res
