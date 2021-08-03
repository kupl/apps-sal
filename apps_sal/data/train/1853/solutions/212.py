class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Dijkstra solution from https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/discuss/536542/Python3-Easy-Readable-Dijkstra
        # Time Complexity: Dijkstra on one vertex is O(ElogV), so for all vertices is O(VElogV), The description says 1 <= edges.length <= n * (n - 1) / 2, so O(E) = O(V^2), Therefore, the final time complexity is O(V^3logV) which should be slower than Floyd Warshall (O(V^3)), comment from https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/discuss/490283/Java-PriorityQueue-%2B-BFS
        graph = collections.defaultdict(list)

        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        def getNumberOfNeighbors(city):
            heap = [(0, city)]
            dist = {}

            while heap:
                currW, u = heapq.heappop(heap)
                if u in dist:  # visited, skip it
                    continue
                if u != city:
                    dist[u] = currW
                for v, w in graph[u]:
                    if v in dist:
                        continue
                    if currW + w <= distanceThreshold:  # find new reacheable city
                        heapq.heappush(heap, (currW + w, v))
            return len(dist)

        return max([(getNumberOfNeighbors(city), city) for city in range(n)], key=lambda x: (-x[0], x[1]))[-1]
