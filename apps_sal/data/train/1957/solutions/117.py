class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m ,n = len(grid), len(grid[0])
        if m == n == 1:
            return 0
        queue = [(0, 0, k)]
        visited = set((0,0))
        steps = 0
        
        while queue:
            new_queue = []
            for x, y, obs in queue:
                for i, j in ((x+1,y), (x-1, y), (x, y+1), (x, y-1)):
                    if 0 <= i < m and  0 <= j < n:
                        if grid[i][j] == 1 and obs > 0 and (i, j, obs - 1) not in visited:
                            new_queue.append((i, j, obs - 1))
                            visited.add((i,j, obs - 1))
                        if grid[i][j] == 0 and (i,j,obs) not in visited:
                            if i == m-1 and j == n-1:
                                return steps + 1
                            visited.add((i, j, obs))
                            new_queue.append((i, j, obs))
                            
            if new_queue:
                queue = new_queue
                steps += 1
            else:
                break
                
        return -1

