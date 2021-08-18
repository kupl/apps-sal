class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        heap = []
        heapq.heappush(heap, (0, 0, 0, k))

        m = len(grid)
        n = len(grid[0])
        visited = set()
        while heap:
            cost, i, j, k = heapq.heappop(heap)

            if (i, j) == (m - 1, n - 1):
                return(cost)

            if (i, j, k) in visited:
                continue

            visited.add((i, j, k))

            for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                x_new = x + i
                y_new = y + j

                if 0 <= x_new < m and 0 <= y_new < n:
                    if grid[x_new][y_new] == 0:
                        heapq.heappush(heap, (cost + 1, x_new, y_new, k))
                    elif grid[x_new][y_new] and k:
                        heapq.heappush(heap, (cost + 1, x_new, y_new, k - 1))
        return -1
