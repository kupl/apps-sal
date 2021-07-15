def isValid(i, j, visited, grid):
    m, n = len(grid), len(grid[0])
    return i >= 0 and j >= 0 and i < m and j < n and grid[i][j] and (i,j) not in visited

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        self.ans = 0
        
        def dfs(i, j, curr_sum, visited):
            if not isValid(i, j, visited, grid):
                return curr_sum
            curr_sum += grid[i][j]
            visited.add((i,j))
            curr_ans = 0
            for x,y in directions:
                newX, newY = i+x, j+y
                curr_ans = max(dfs(newX, newY, curr_sum, visited), curr_ans)
            self.ans = max(curr_ans, self.ans)
            visited.remove((i,j))
            return curr_ans
        
        for r in range(m):
            for c in range(n):
                dfs(r, c, 0, set())
        return self.ans
