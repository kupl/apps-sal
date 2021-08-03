class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        def dfs(x, y, delete, used, dp):
            if x == len(grid) - 1 and y == len(grid[0]) - 1:
                return 0
            if (x, y, delete) in dp:
                return dp[(x, y, delete)]
            result = float('inf')

            if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                if grid[x][y] == 1:
                    if delete == 0:
                        dp[(x, y, delete)] = float('inf')
                        return float('inf')
                    delete -= 1

                used.add((x, y))
                for dx, dy in step:
                    tx = x + dx
                    ty = y + dy
                    if (tx, ty) not in used:
                        result = min(result, dfs(tx, ty, delete, used, dp) + 1)
                used.remove((x, y))
                dp[(x, y, delete)] = result
            return result

        shortest = len(grid) + len(grid[0]) - 2
        if k >= shortest:
            return shortest
        step = [[1, 0], [0, 1], [0, -1], [-1, 0]]
        res = dfs(0, 0, k, set(), {})
        return res if res != float('inf') else -1
