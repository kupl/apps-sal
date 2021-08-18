from collections import defaultdict


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        '''
            return the city with the smallest number of cities that are reachable through some path
            Dijkstra
        '''
        graph = defaultdict(dict)
        for city1, city2, weight in edges:
            graph[city1][city2] = weight
            graph[city2][city1] = weight

        res, res_reachable = None, float('inf')
        for i in range(n):
            visited = set()
            unvisited = set()
            shortest_distance = [float('inf')] * n
            for j in range(n):
                if j == i:
                    visited.add(j)
                    shortest_distance[i] = 0
                else:
                    unvisited.add(j)
            cur = i
            reachable = defaultdict(set)
            while cur != None:
                for neighbor in graph[cur]:
                    if neighbor not in visited:
                        if shortest_distance[cur] + graph[cur][neighbor] <= distanceThreshold:
                            reachable[i].add(neighbor)
                            if shortest_distance[cur] + graph[cur][neighbor] < shortest_distance[neighbor]:
                                shortest_distance[neighbor] = shortest_distance[cur] + graph[cur][neighbor]

                cur = None
                for city in unvisited:
                    if shortest_distance[city] != float('inf'):
                        if cur == None:
                            cur = city
                        else:
                            if shortest_distance[city] < shortest_distance[cur]:
                                cur = city
                if cur != None:
                    visited.add(cur)
                    unvisited.remove(cur)

            if len(reachable[i]) <= res_reachable:
                res_reachable = len(reachable[i])
                res = i

        return res
