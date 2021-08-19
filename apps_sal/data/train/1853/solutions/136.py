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

        print([(self.getNumberOfNeighbors(city, graph, distanceThreshold), city) for city in range(n)])  # [(2, 0), (3, 1), (3, 2), (2, 3)] -> len(dist), city
        print(max([(self.getNumberOfNeighbors(city, graph, distanceThreshold), city) for city in range(n)]))  # (3, 2)
        print(max([(self.getNumberOfNeighbors(city, graph, distanceThreshold), city) for city in range(n)], key=lambda x: (-x[0], x[1])))  # (2, 3)

        return max([(self.getNumberOfNeighbors(city, graph, distanceThreshold), city) for city in range(n)], key=lambda x: (-x[0], x[1]))[-1]  # least distance dict, but max city number

    def getNumberOfNeighbors(self, city, graph, distanceThreshold):
        heap = [(0, city)]
        dist = {}

        while heap:
            currW, visitedCity = heapq.heappop(heap)
            if visitedCity in dist:
                continue
            if city != visitedCity:
                dist[visitedCity] = currW
            for neighborCity, w in graph[visitedCity]:
                if neighborCity in dist:
                    continue
                if currW + w <= distanceThreshold:
                    heapq.heappush(heap, (currW + w, neighborCity))
        return len(dist)
