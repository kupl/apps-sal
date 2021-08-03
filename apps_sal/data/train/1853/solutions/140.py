import heapq


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        def djikstras(matrix, cities, src):
            vertices = []
            visited = []
            heapq.heappush(vertices, (0, src))
            while vertices:
                vertexDist, vertex = heapq.heappop(vertices)
                if vertex in visited:
                    continue
                visited.append(vertex)
                if vertexDist <= distanceThreshold:
                    cities.append(vertex)
                    if vertex in matrix:
                        for (v, w) in matrix[vertex]:
                            newDist = vertexDist + w
                            heapq.heappush(vertices, (newDist, v))
            return cities

        cityList = []
        finalCityList = []
        matrix = {}
        for edge in edges:
            if edge[0] not in matrix:
                matrix[edge[0]] = []
            matrix[edge[0]].append((edge[1], edge[2]))
            # This line holds good only if the graph is bidirectional
            if edge[1] not in matrix:
                matrix[edge[1]] = []
            matrix[edge[1]].append((edge[0], edge[2]))
        for i in range(n):
            cities = djikstras(matrix, [], i)
            #print(cities, i)
            # Removing source city
            if cities:
                heapq.heappush(cityList, (len(cities), i * -1))
            # print(cityList)

        return heapq.heappop(cityList)[1] * -1
