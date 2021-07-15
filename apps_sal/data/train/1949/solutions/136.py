class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        final = [0]
        visited = set()
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        def bt(current_sum = 0, i=0, j=0):
            if (i,j) in visited or i<0 or i>=len(grid) or j<0 or j>= len(grid[0]) or grid[i][j]==0:
                final[0] =max(final[0],current_sum)
                return
            current_sum+=grid[i][j]
            visited.add((i,j))
            for direction in directions:
                new_i = i+direction[0]
                new_j = j+direction[1]
                bt(current_sum,new_i,new_j)
            visited.remove((i,j))
            current_sum-=grid[i][j]
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                bt(i=row,j=col)
        return final[0]

