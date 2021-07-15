class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        def is_valid(i, j):
            if 0 <= i < m and 0 <= j < n:
                return True
            return False
        
        def dfs(i, j, visited, cur_sum):
            visited.add((i, j))
            cur_sum += grid[i][j]
            
            cur_max = 0
            for d in directions:
                ni, nj = i+d[0], j+d[1]
                if is_valid(ni,nj) and (ni,nj) not in visited and grid[ni][nj]>0:
                    cur_max = max(cur_max, dfs(ni, nj, visited, cur_sum))
                else:
                    cur_max = max(cur_max, cur_sum)
            visited.discard((i, j))
            return cur_max
            
        m, n = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        max_gold = 0
        visited = set()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    max_gold = max(max_gold, dfs(i, j, set(), 0))
                    
        return max_gold
