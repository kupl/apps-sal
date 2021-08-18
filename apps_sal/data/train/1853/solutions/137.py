class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        import collections
        '''
        graph = collections.defaultdict(list)
        
        for edge in edges:
            graph[edge[0]].append([edge[1]], edge[2])
        
        res = []
        
        for i in range(n):
        '''

        graph = collections.defaultdict(list)

        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        print([(self.getNumberOfNeighbors(city, graph, distanceThreshold), city) for city in range(n)])
        print(max([(self.getNumberOfNeighbors(city, graph, distanceThreshold), city) for city in range(n)]))
        print(max([(self.getNumberOfNeighbors(city, graph, distanceThreshold), city) for city in range(n)], key=lambda x: (-x[0], x[1])))

        return max([(self.getNumberOfNeighbors(city, graph, distanceThreshold), city) for city in range(n)], key=lambda x: (-x[0], x[1]))[-1]

    def getNumberOfNeighbors(self, city, graph, distanceThreshold):
        heap = [(0, city)]
        dist = {}

        while heap:
            currW, u = heapq.heappop(heap)
            if u in dist:
                continue
            if u != city:
                dist[u] = currW
            for v, w in graph[u]:
                if v in dist:
                    continue
                if currW + w <= distanceThreshold:
                    heapq.heappush(heap, (currW + w, v))
        return len(dist)
