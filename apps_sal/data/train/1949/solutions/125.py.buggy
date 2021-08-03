class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(i: int, j: int, sum: int, seen: set) -> int:
            if i < 0 or i >= m or j < 0 or j >= n or not grid[i][j] or (i, j) in seen:
                return sum 
            seen.add((i, j))
            sum += grid[i][j]
            mx = 0
            for x, y in ((i, j + 1), (i , j - 1), (i + 1, j), (i - 1, j)):
                mx = max(dfs(x, y, sum, seen), mx)
            seen.remove((i, j)) 
            return mx

        m, n = len(grid), len(grid[0])
        return max(dfs(i, j, 0, set()) for j in range(n) for i in range(m))
    
    \"\"\"
    Loop through the grid, for each element at (i, j) perform DFS to get the max value;
if (i, j) is out of the bound, or grid[i][j] == 0, or visited already, return current sum;
Otherwise, recurse to the neighbors and accumulate the sum.
    \"\"\"
    
    \"\"\"
    Each of the k gold cells can at most have 4 neighbors. Therefore,
Time: O(k * 4 ^ k + m * n), space: O(m * n), where k = number of gold cells, m = grid.length, n = grid[0].length.
    \"\"\"
    
