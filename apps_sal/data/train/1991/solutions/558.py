import functools


class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        graph = dict()
        for i in range(len(locations)):
            if i not in graph:
                graph[i] = dict()
            for j in range(len(locations)):
                if i != j:
                    graph[i][j] = abs(locations[i] - locations[j])

        @functools.lru_cache(None)
        def bfs(position: int, fuel: int, count: int) -> int:
            if position == finish:
                res = count
            else:
                res = 0
            for neighbor in graph[position]:
                if fuel >= graph[position][neighbor]:
                    res += bfs(neighbor, fuel - graph[position][neighbor], count)
            return res
        return bfs(start, fuel, 1) % (10 ** 9 + 7)
