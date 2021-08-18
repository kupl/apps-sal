class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        for k in graph:
            graph[k].sort(key=lambda x: x[1])

        def dijk(i, budget):
            seen, pq = set(), [(0, i, 0)]
            while pq:
                cost, u, steps = heapq.heappop(pq)
                seen.add(u)
                for nei, weight in graph[u]:
                    if nei in seen or cost + weight > budget:
                        continue
                    else:
                        heapq.heappush(pq, (cost + weight, nei, steps + 1))

            return len(seen)

        min_city, ans = n, None
        for i in range(n):
            n_reachable = dijk(i, distanceThreshold)
            if n_reachable <= min_city:
                min_city, ans = n_reachable, i
        return ans
