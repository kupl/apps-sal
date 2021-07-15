class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = collections.defaultdict(set)
        for u, v, w in edges: 
            graph[u].add((v, w))
            graph[v].add((u, w))
            
        def dijk(i, budget): 
            seen, pq = set(), [(0, i, 0)]
            while pq: 
                cost, u, steps = heapq.heappop(pq)
                seen.add(u)
                for nei, weight in graph[u]: 
                    if nei in seen or cost + weight > budget: 
                        continue
                    heapq.heappush(pq, (cost + weight, nei, steps + 1))
            return len(seen)
            
        min_city, ans = n, None
        for i in range(n): 
            n_reachable = dijk(i, distanceThreshold)
            if n_reachable <= min_city: 
                min_city, ans = n_reachable, i
        return ans
            
    # def findTheCity(self, n, edges, maxd):
    #     dis = [[float('inf')] * n for _ in range(n)]
    #     for i, j, w in edges:
    #         dis[i][j] = dis[j][i] = w
    #     for i in range(n):
    #         dis[i][i] = 0
    #     for k in range(n):
    #         for i in range(n):
    #             for j in range(n):
    #                 dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
    #     res = {sum(d <= maxd for d in dis[i]): i for i in range(n)}
    #     return res[min(res)]

