class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        if not grid or not grid[0]:
            return 0
        n = len(grid)
        m = len(grid[0])
        hp = []
        heapq.heappush(hp, (0, 0, 0, 0))
        visited = set()
        visited.add((0, 0, 0))
        while hp:
            step, d, i, j = heapq.heappop(hp)
            if i == n - 1 and j == m - 1:
                return step
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if x < 0 or x >= n or y < 0 or y >= m or (x, y, d + grid[x][y]) in visited or grid[x][y] + d > k:
                    continue
                visited.add((x, y, grid[x][y] + d))
                heapq.heappush(hp, (step + 1, d + grid[x][y], x, y))
        return -1

