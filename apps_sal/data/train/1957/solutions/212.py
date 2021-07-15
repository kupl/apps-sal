from queue import Queue

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])
        q = Queue()
        if k == 0 and grid[0][0] == 1:
            return -1
        shortest_path = dict()
        def get_neighbors(r, c):
            neighbors = []
            for ri, ci in [(r-1, c), (r, c-1), (r+1, c), (r, c+1)]:
                if ri < 0 or ci < 0 or ri == n or ci == m:
                    continue
                neighbors.append((ri, ci))
            return neighbors
        
        q.put((0,0,grid[0][0]))
        shortest_path[(0,0,grid[0][0])]=0
        while q.qsize() > 0:
            r, c, d = q.get()
            if r == n-1 and c == m-1:
                return shortest_path[(r,c,d)]
            neighbors = get_neighbors(r,c)
            for ri, ci in neighbors:
                if d+grid[r][c] > k or (ri, ci, d+grid[r][c]) in shortest_path:
                    continue
                q.put((ri, ci, d+grid[r][c]))
                shortest_path[(ri, ci, d+grid[r][c])] = shortest_path[(r,c,d)] + 1
        return -1                
