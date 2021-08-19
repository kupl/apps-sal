class Solution:

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        maps = [[2 ** 30] * n for _ in range(n)]
        nums_neighbors = [0] * n
        for i in range(n):
            maps[i][i] = 0
        for info in edges:
            (src, dst, cost) = info
            maps[src][dst] = cost
            maps[dst][src] = cost
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    maps[j][k] = min(maps[j][k], maps[j][i] + maps[i][k])
        min_idx = 0
        for i in range(n):
            nums_neighbors[i] = len([x for x in maps[i] if x != 0 and x <= distanceThreshold])
            if nums_neighbors[i] <= nums_neighbors[min_idx]:
                min_idx = i
        return min_idx
