class Solution:

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        from collections import defaultdict
        graph = defaultdict(list)
        for (start, finish, distance) in edges:
            graph[start].append([distance, finish])
            graph[finish].append([distance, start])
        reachable_within_threashold = {}
        import heapq
        for house in range(n):
            if house not in graph:
                continue
            else:
                heap = [[0, house]]
                reachable_from_this_house = []
                while heap:
                    (distance_sofar, cur_house) = heapq.heappop(heap)
                    if distance_sofar > distanceThreshold:
                        continue
                    if cur_house in reachable_from_this_house:
                        continue
                    if cur_house in graph:
                        for (dis, neighbor) in graph[cur_house]:
                            if neighbor not in reachable_from_this_house:
                                heapq.heappush(heap, [dis + distance_sofar, neighbor])
                    if cur_house != house:
                        reachable_from_this_house.append(cur_house)
            reachable_within_threashold[house] = reachable_from_this_house
        for house in range(n - 1, -1, -1):
            if house not in reachable_within_threashold:
                return house
        min_ = float('inf')
        result = float('inf')
        for house in range(n - 1, -1, -1):
            cur_no = len(reachable_within_threashold[house])
            if cur_no < min_:
                min_ = cur_no
                result = house
        return result
