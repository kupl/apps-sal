from collections import deque
class Solution:
    def shortestPath(self, g: List[List[int]], k: int) -> int:
        m, n = len(g), len(g[0])
        q = collections.deque([(0, 0, k, 0)])
        seen = {(0, 0, k)}
        while q:
            x, y, r, s = q.popleft()
            if x==m-1 and y==n-1:
                return s
            for i, j in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                if 0<=x+i<m and 0<=y+j<n:
                    nr = r-(g[x+i][y+j]==1)
                    if (x+i, y+j, nr) not in seen and nr>=0:
                        q.append((x+i, y+j, nr, s+1))
                        seen.add((x+i, y+j, nr))
        return -1
#     def shortestPath(self, grid: List[List[int]], k: int) -> int:
#         m, n = len(grid), len(grid[0])
#         move = [(0,1), (1,0), (0,-1), (-1,0)]
#         visited = set([])
#         q = deque([(0,0,0,k)])
#         while q:
#             r, c, cur, cur_k = q.popleft()
#             visited.add((r,c,cur_k))
#             if r == m-1 and c == n-1:
#                 return cur
#             for dx, dy in move:
#                 row, col = r+dy, c+dx
#                 if 0<= row < m and 0 <= col < n:
                
#                     if grid[row][col] == 1 and cur_k > 0 and \\
#                     (row, col, cur_k-1) not in visited:
#                         q.append((row, col, cur+1, cur_k-1))
#                         visited.add((row, col, cur_k-1))
#                     if grid[row][col] == 0 and (row, col, cur_k) not in visited:
#                         if row == m-1 and col == n-1:
#                             return cur + 1
#                         q.append((row, col, cur+1, cur_k))
#                         visited.add((row, col, cur_k))
                        
        
#         return -1

