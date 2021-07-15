class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        if len(grid) == 1 and len(grid[0]) == 1:
            return 0
        visited = set()
        q = collections.deque([(0,0,0,0)])
        r,c = len(grid), len(grid[0])
        while q:
            x, y, obs, path = q.popleft()
            for i, j in [(x,y+1),(x,y-1),(x+1,y),(x-1,y)]:
                if 0 <= i < r and 0 <= j < c:
                    if grid[i][j] == 0 and (i,j,obs) not in visited:
                        if i == r- 1 and j == c - 1:
                            return path+1   
                        q.append([i,j,obs,path+1])
                        visited.add((i,j,obs))
                    if grid[i][j] == 1 and obs < k and ((i,j,obs+1) not in visited):
                        q.append([i,j,obs+1,path+1])
                        visited.add((i,j,obs+1))
        return -1 
