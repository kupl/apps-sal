class Solution:

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        weight = collections.defaultdict(dict)
        for (u, v, w) in edges:
            weight[u][v] = w
            weight[v][u] = w

        def getNumberOfNeighbors(city):
            heap = [(0, city)]
            dist = {}
            while heap:
                (w, u) = heapq.heappop(heap)
                if u not in dist and u != city:
                    dist[u] = w
                for v in weight[u]:
                    if v in dist:
                        continue
                    if w + weight[u][v] <= distanceThreshold:
                        heapq.heappush(heap, (w + weight[u][v], v))
            return len(dist)
        minCount = float('inf')
        ans = None
        for i in range(n):
            count = getNumberOfNeighbors(i)
            if count <= minCount:
                ans = i
                minCount = count
        return ans
