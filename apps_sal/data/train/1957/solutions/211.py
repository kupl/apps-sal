class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        dst = (len(grid) - 1, len(grid[0]) - 1)
        heap = [(0, 0, (0, 0))]  # cost, stop, node
        cost_map = collections.defaultdict(lambda: float('inf'))
        while heap:
            cost, stop, node = heapq.heappop(heap)
            if stop > k or cost >= cost_map[(stop, node)]:
                continue
            if node == dst:
                return cost
            cost_map[(stop, node)] = cost
            i, j = node
            for n_i, n_j in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if n_i < 0 or n_j < 0 or n_i >= m or n_j >= n:
                    continue
                if (n_i, n_j) == dst:
                    return cost + 1
                if grid[n_i][n_j] == 0:
                    heapq.heappush(heap, (cost + 1, stop, (n_i, n_j)))
                else:
                    if stop + 1 <= k:
                        heapq.heappush(heap, (cost + 1, stop + 1, (n_i, n_j)))

        return -1
