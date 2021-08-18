class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], threshold: int) -> int:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        def dijkstra(initial_node):
            dist = [float('inf')] * n
            dist[initial_node] = 0

            pq = [(initial_node, 0)]
            while pq:
                node, d = heappop(pq)

                for adjnode, weight in graph[node]:
                    if dist[adjnode] > dist[node] + weight:
                        dist[adjnode] = dist[node] + weight
                        pq.append((adjnode, dist[node]))
            return dist

        city_num = 0
        cc = n + 1
        for node in range(n):
            dist = dijkstra(node)
            print(dist)
            c = -1
            for d in dist:
                if d <= threshold:
                    c += 1

            if c <= cc:
                print(c)
                cc = c
                city_num = node

        return city_num
