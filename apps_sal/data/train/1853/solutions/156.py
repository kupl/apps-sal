class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        def getNumberOfNeighbors(city, graph):
            heap = [(0, city)]
            dist = {}

            while heap:
                currW, u = heapq.heappop(heap)
                if u in dist:
                    continue
                if u != city:
                    dist[u] = currW
                for v, w in graph[u].items():
                    if v in dist:
                        continue
                    if currW + w <= distanceThreshold:
                        heapq.heappush(heap, (currW + w, v))
            return len(dist)

        adjList = collections.defaultdict(dict)
        for start, end, weight in edges:
            adjList[start][end] = weight
            adjList[end][start] = weight

        disconnected_cities = set([i for i in range(n)]) - adjList.keys()
        if disconnected_cities:
            return max(disconnected_cities)

        min_so_far = float('inf')
        cities = []

        for city in adjList.keys():
            count = getNumberOfNeighbors(city, adjList)

            if count < min_so_far:
                min_so_far = count
                cities = [city]
            elif count == min_so_far:
                cities.append(city)
        return max(cities)
