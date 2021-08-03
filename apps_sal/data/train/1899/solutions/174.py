class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def dfs(curr_i, curr_j, outliners):
            visited.add((curr_i, curr_j))
            for delta_i, delta_j in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
                next_i, next_j = curr_i + delta_i, curr_j + delta_j
                if 0 <= next_i < m and 0 <= next_j < n:
                    if grid[next_i][next_j] == 0:
                        outliners.add((next_i, next_j))
                    elif grid[next_i][next_j] == 1:
                        if (next_i, next_j) not in visited:
                            dfs(next_i, next_j, outliners)

        m, n = len(grid), len(grid[0])
        visited = set()
        outliners_1, outliners_2 = set(), set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    if len(outliners_1) == 0:
                        dfs(i, j, outliners_1)
                    else:
                        dfs(i, j, outliners_2)

        min_dist = m + n
        for (i, j) in outliners_1:
            for (p, q) in outliners_2:
                min_dist = min(min_dist, abs(i - p) + abs(j - q) + 1)
        return min_dist
