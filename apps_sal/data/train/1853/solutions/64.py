class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], threeshold: int) -> int:
        class Graph:
            def __init__(self, vertices):
                self.v = vertices
                self.graph = collections.defaultdict(dict)

            def add_edge(self, u, v, cost):
                self.graph[u][v] = cost
                self.graph[v][u] = cost

            def calculateDist(self, s, dT):
                dist = [sys.maxsize] * (self.v)
                dist[s] = 0
                unvisited_queue = [[0, s]]
                visited = [False] * self.v
                heapq.heapify(unvisited_queue)
                while len(unvisited_queue) > 0:
                    u = heapq.heappop(unvisited_queue)
                    curr_v = u[1]
                    visited[curr_v] = True
                    for neighbour in self.graph[curr_v]:
                        cost = self.graph[curr_v][neighbour]
                        if dist[neighbour] > dist[curr_v] + cost:
                            dist[neighbour] = dist[curr_v] + cost
                    while len(unvisited_queue) > 0:
                        heapq.heappop(unvisited_queue)
                    for node in range(self.v):
                        if visited[node] == False:
                            heapq.heappush(unvisited_queue, [dist[node], node])
                cities = -1
                for d in dist:
                    if d <= dT:
                        cities += 1
                return cities
        min_connections = sys.maxsize
        city = 0
        v = n
        graph = Graph(v)
        for edge in edges:
            n, m, cost = edge[0], edge[1], edge[2]
            graph.add_edge(n, m, cost)
        for i in range(v):
            cities = graph.calculateDist(i, threeshold)
            if cities < min_connections:
                min_connections = cities
                city = i
            elif cities == min_connections:
                city = max(city, i)
        return city
