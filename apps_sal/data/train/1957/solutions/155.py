class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        visited = set()
        mem = {}
        MAX_NUM = float(\"inf\")
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        def dfs(i, j, k):
            if i == len(grid)-1 and j == len(grid[0])-1:
                return len(visited)

            if (i,j,k) in mem:
                return mem[(i,j,k)]

            if (i, j) in visited:
                return MAX_NUM

            if i < 0 or j < 0 or  i >= len(grid) or j >= len(grid[0]):
                return  MAX_NUM

            if grid[i][j] == 1 and k == 0:
                return MAX_NUM

            if grid[i][j] == 1:
                k -= 1

            min_steps = MAX_NUM
            visited.add((i,j))
            for di, dj in directions:
                min_steps = min(min_steps, dfs(i+di, j+dj, k))
            visited.remove((i,j))

            mem[(i,j,k)] = min_steps

            return min_steps
        
        def bfs(i, j, k):
            q = []
            q.append((i,j,k,0))
            visited.add((i,j,k))
            
            while len(q) > 0:
                curr_i, curr_j, curr_k, depth = q.pop(0)
                
                if curr_i < 0 or curr_j < 0 or  curr_i >= len(grid) or curr_j >= len(grid[0]):
                    continue
                
                if grid[curr_i][curr_j] == 1 and curr_k == 0:
                    continue
                
                if curr_i == len(grid)-1 and curr_j == len(grid[0])-1:
                    print(curr_k)
                    return depth
                
                new_k = curr_k
                if grid[curr_i][curr_j] == 1:
                    new_k -= 1
                    
                for di, dj in directions:
                    if (curr_i+di, curr_j+dj, new_k) not in visited:
                        q.append((curr_i+di, curr_j+dj, new_k, depth+1))
                        visited.add((curr_i+di, curr_j+dj,new_k))
            return -1

        return bfs(0,0,k)
    
#         res = dfs(0,0,k)
#         if res == MAX_NUM:
#             return -1
        
#         return res

        
