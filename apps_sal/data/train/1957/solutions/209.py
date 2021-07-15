import queue
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        q = queue.Queue()
        
        q.put([0, 0, k, 0]) # row, col, k, level
        visited = set()
        dir_ = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        visited.add((0, 0, k))
        while not q.empty():
            r, c, cur_k, level = q.get()
            if r == len(grid) - 1 and c == len(grid[0]) -1:
                return level
            for x, y in dir_:
                nr, nc = x + r, y + c
                if not (0 <= nr < len(grid) and 0 <= nc < len(grid[0])) :
                    continue 
                    
                if grid[nr][nc] == 1 and cur_k > 0 and (nr, nc, cur_k-1) not in visited:
                    q.put([nr, nc, cur_k-1, level+1])
                    visited.add((nr, nc, cur_k-1))
                if grid[nr][nc] == 0 and (nr, nc, cur_k) not in visited:
                    q.put([nr, nc, cur_k, level+1])
                    visited.add((nr, nc, cur_k))
                if nr == len(grid) - 1 and nc == len(grid[0]) - 1:
                    return level + 1
        return -1 
