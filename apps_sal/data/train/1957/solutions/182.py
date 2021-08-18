class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        heap = [(0, 0, 0, 0)]
        seen = set()
        while heap:
            c, used, i, j = heapq.heappop(heap)
            if (i, j, used) in seen:
                continue
            if i == n - 1 and j == m - 1:
                return c
            seen.add((i, j, used))
            for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= ni < n and 0 <= nj < m and used + grid[ni][nj] <= k and (ni, nj, used + grid[ni][nj]) not in seen:
                    heapq.heappush(heap, (c + 1, used + grid[ni][nj], ni, nj))

        return -1
