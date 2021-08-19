from heapq import *


class Solution:

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        def find_n_neigh(source_city):
            visited = set()
            pq = [(0, source_city)]
            while pq:
                (trav_dist, curr_city) = heappop(pq)
                if curr_city in visited:
                    continue
                if curr_city != source_city:
                    visited.add(curr_city)
                for (neigh, distance) in graph[curr_city]:
                    if neigh not in visited and trav_dist + distance <= distanceThreshold:
                        heappush(pq, (trav_dist + distance, neigh))
            return len(visited)
        graph = defaultdict(list)
        for (city, neigh, distance) in edges:
            graph[city].append((neigh, distance))
            graph[neigh].append((city, distance))
        n_neighs = [find_n_neigh(city) for city in range(n)]
        min_n = min(n_neighs)
        return [city for city in range(n) if n_neighs[city] == min_n][-1]
