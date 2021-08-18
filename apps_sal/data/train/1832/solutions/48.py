class Solution:
    def reachableNodes(self, edges: List[List[int]], M: int, N: int) -> int:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        min_heap = [(0, 0)]
        min_dist = [M + 1] * N
        min_dist[0] = 0

        edge2used = defaultdict(int)
        res = 0
        while min_heap:
            dist, u = heapq.heappop(min_heap)
            if dist > min_dist[u]:
                continue

            res += 1

            for v, w in graph[u]:
                used = min(M - dist, w)
                edge2used[(u, v)] = used
                dist_v = dist + w + 1
                if dist_v < min_dist[v]:
                    min_dist[v] = dist_v
                    heapq.heappush(min_heap, (dist_v, v))

        for u, v, w in edges:
            res += min(w, edge2used[u, v] + edge2used[v, u])

        return res
