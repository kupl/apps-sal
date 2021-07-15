from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        move = [(0,1), (1,0), (0,-1), (-1,0)]
        visited = set([])
        q = deque([(0,0,0,k)])
        while q:
            r, c, cur, cur_k = q.popleft()
            visited.add((r,c,cur_k))
            if r == m-1 and c == n-1:
                return cur
            for dx, dy in move:
                row, col = r+dy, c+dx
                if 0<= row < m and 0 <= col < n:
                
                    if grid[row][col] == 1 and cur_k > 0 and \\
                    (row, col, cur_k-1) not in visited:
                        q.append((row, col, cur+1, cur_k-1))
                        visited.add((row, col, cur_k-1))
                    if grid[row][col] == 0 and (row, col, cur_k) not in visited:
                        q.append((row, col, cur+1, cur_k))
                        visited.add((row, col, cur_k))
                        
        
        return -1
