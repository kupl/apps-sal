class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        graph = collections.defaultdict(list)
        for u, v, w in edges:
            graph[u].append([w, v])
            graph[v].append([w, u])
        count = [0] * n

        def find_cities_k(vertex, vis):
            q = []
            heapq.heappush(q, [0, vertex])
            while q:
                dis, node = heapq.heappop(q)
                if node in vis:
                    continue
                vis.add(node)
                if dis <= distanceThreshold:
                    if vertex != node:
                        count[vertex] += 1
                for w, neigh in graph[node]:
                    if neigh not in vis:
                        heapq.heappush(q, [dis + w, neigh])
        for i in range(n):
            find_cities_k(i, set())
        min_ = 10000
        city_ = -1
        for i in range(n):
            if count[i] <= min_:
                min_ = count[i]
                city_ = i
        return city_
