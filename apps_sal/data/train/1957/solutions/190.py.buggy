from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        x_a = [1, 0, -1, 0]
        y_a = [0, -1, 0, 1]
        
        visited = {\"0 0 0\"}
        nbours = [(0,0,0)]
        steps = 0
        while nbours:            
            new_nbours = []
            for coord in nbours:
                if coord[0] == len(grid[0]) - 1 and coord[1] == len(grid) - 1:
                    return steps
                for x, y in zip(x_a, y_a):
                    new_x = coord[0] + x
                    new_y = coord[1] + y
                    if 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid):
                        new_k = coord[2] + 1
                        if grid[new_y][new_x] == 1:
                            if new_k <= k:
                                new_coord = (new_x, new_y, new_k)
                            else:
                                continue
                        else:
                            new_coord = (new_x, new_y, coord[2])
                        s = str(new_coord[0]) + \" \" + str(new_coord[1]) + \" \" +  str(new_coord[2])
                        if s not in visited:
                            new_nbours.append(new_coord)
                            visited.add(s)
            steps += 1
            nbours = new_nbours
        return -1
            
            
                    
