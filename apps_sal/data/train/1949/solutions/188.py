def isValid(i, j, n, m):
    return i >= 0 and j >= 0 and i < n and j < m


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        n, m = len(grid), len(grid[0])

        def dfs(i, j, curr_sum, visited):
            if not isValid(i, j, n, m) or (i, j) in visited or not grid[i][j]:
                return curr_sum
            curr_sum += grid[i][j]
            final = 0
            visited.add((i, j))
            for x, y in directions:
                newX, newY = i + x, j + y
                final = max(dfs(newX, newY, curr_sum, visited), final)
            visited.remove((i, j))
            return final

        ans = 0
        visited = set()
        for r in range(n):
            for c in range(m):
                ans = max(ans, dfs(r, c, 0, visited))
        return ans
