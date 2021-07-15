class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.ans = 0
        seen = set()
        delta = [(1,0), (-1,0), (0,-1), (0,1)]
        def dfs(i,j,cur=0):
            
            for di, dj in delta:
                new_i, new_j = i + di, j + dj
                if 0 <= new_i < len(grid) and 0 <= new_j < len(grid[0]):
                    if (new_i, new_j) not in seen and grid[new_i][new_j]:
                        seen.add((new_i, new_j))
                        cur += grid[new_i][new_j]
                        self.ans = max(self.ans, cur)
                        dfs(new_i, new_j, cur)
                        cur -= grid[new_i][new_j]
                        seen.remove((new_i, new_j))
            return 
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and (i,j) not in seen:
                    seen.add((i,j))
                    self.ans = max(self.ans, grid[i][j])
                    dfs(i,j, grid[i][j])
                    seen.remove((i,j))
        return self.ans
                
            
            
            


