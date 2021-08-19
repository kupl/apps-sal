class Solution:

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = collections.defaultdict(list)
        for (u, v, w) in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        dist = collections.defaultdict(list)
        self.min = float('inf')

        def getNumberOfNeighbors(city):
            heap = [(0, city)]
            count = 0
            seen = set()
            while heap:
                (currW, u) = heapq.heappop(heap)
                if u in seen:
                    continue
                seen.add(u)
                for (v, w) in graph[u]:
                    if v in seen:
                        continue
                    if currW + w <= distanceThreshold:
                        heapq.heappush(heap, (currW + w, v))
                count += 1
            return count
        for city in range(n):
            num = getNumberOfNeighbors(city)
            dist[num].append(city)
            self.min = min(self.min, num)
        return max(dist[self.min])
