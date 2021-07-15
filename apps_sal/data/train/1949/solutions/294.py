class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        
        def dfs(path, curr_sum):
            nonlocal res
            
            i, j = path[-1]
            dirs_lst = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            find = False
            for di, dj in dirs_lst:
                ni = i+di
                nj = j+dj
                if 0<=ni<M and 0<=nj<N and grid[ni][nj]>0:
                    # if (i==1 and j==2):
                    #     print (path, grid[ni][nj], grid)
                    find = True
                    curr_sum += grid[ni][nj]
                    grid[ni][nj] = -grid[ni][nj]
                    # vis.add((ni, nj))
                    # print (path, curr_sum)
                    path.append((ni, nj))
                    dfs(path, curr_sum)
                    path.pop()
                    grid[ni][nj] = -grid[ni][nj]
                    curr_sum -= grid[ni][nj]
            if not find:
                # if curr_sum==35:
                #     print ('aa ', path, curr_sum)
                res = max(res, curr_sum)
        
        
        
        res = 0
        M = len(grid)
        N = len(grid[0])
        for i in range(M):
            for j in range(N):
                if grid[i][j]>0:
                    # vis = set()
                    grid[i][j] = -grid[i][j]
                    dfs([(i, j)], -grid[i][j])
                    grid[i][j] = -grid[i][j]
                    # for x, y in vis:
                    #     grid[x][y] = 0
                    
        return res

