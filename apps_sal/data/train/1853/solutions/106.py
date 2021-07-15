


from heapq import *
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        def find_n_neighbours(source_city):

            visited = set()
            heap = [(0, source_city)]

            while heap:
                travelled_distance, curr_city = heappop(heap)
                if curr_city in visited:
                    continue

                if curr_city != source_city:
                    visited.add(curr_city)

                for neigh, distance in graph[curr_city]:
                    if neigh in visited:
                        continue

                    if travelled_distance + distance <= distanceThreshold:
                        heappush(heap, (travelled_distance + distance, neigh))

            return len(visited)

        graph = defaultdict(list)        
        for from_, to, distance in edges:
            graph[from_].append((to, distance))
            graph[to].append((from_, distance))

        neighbours = [find_n_neighbours(i) for i in range(n) ]
        min_count = min(neighbours)
        sel_cities = [i for i in range(n) if neighbours[i] == min_count]
        return sel_cities[-1]

