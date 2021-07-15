class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        EMPTY, OBSTACLE = 0, 1
        m, n = len(grid), len(grid[0])
        distance = defaultdict(lambda: math.inf)
        distance[0, 0, 0] = 0
        pq = [(0, 0, 0, 0)]
        while pq:
            d, e, i, j = heapq.heappop(pq)
            if distance[e, i, j] < d:
                continue
            if i == m - 1 and j == n - 1:
                return d
            for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= ni < m and 0 <= nj < n:
                    ne = e + int(grid[ni][nj] == OBSTACLE)
                    if ne <= k:
                        nd = d + 1
                        if nd < distance[ne, ni, nj]:
                            distance[ne, ni, nj] = nd
                            heapq.heappush(pq, (nd, ne, ni, nj))
        return -1
