class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(x, y, visited, res):

            maxi = res[::]
            for (i, j) in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if i >= 0 and i < m and j >= 0 and j < n and grid[i][j] > 0 and (i, j) not in visited:
                    visited.add((i, j))
                    res.append(grid[i][j])
                    result = dfs(i, j, visited, res)
                    maxi = maxi if sum(maxi) > sum(result) else result
                    # print(x,y,i,j,result)
                    res.pop()
                    visited.remove((i, j))
            # print(x,y,maxi)
            return maxi

        maxi = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    visited = set()
                    res = []
                    res.append(grid[i][j])
                    visited.add((i, j))
                    result = dfs(i, j, visited, res)
                    # visited.remove((i,j))
                    # print(result)
                    maxi = max(maxi, sum(result))
        return maxi
