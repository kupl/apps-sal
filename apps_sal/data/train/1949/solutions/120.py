class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(pos):
            if grid[pos[0]][pos[1]] == 0:
                return 0
            
            gold = grid[pos[0]][pos[1]]
            grid[pos[0]][pos[1]] = 0
            
            next_pos = [
                (pos[0]-1, pos[1]),
                (pos[0]+1, pos[1]),
                (pos[0], pos[1]-1),
                (pos[0], pos[1]+1),
            ]

            max_child = 0
            for p in next_pos:
                if -1 < p[0] < n and -1 < p[1] < m:
                    max_child = max(max_child, dfs(p))
            
            grid[pos[0]][pos[1]] = gold
            return gold + max_child
        
        n = len(grid)
        m = len(grid[0])
        
        max_gold = 0
        for i in range(n):
            for j in range(m):
                max_gold = max(max_gold, dfs((i, j)))
        return max_gold
