from collections import deque
Directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        queue = deque()
        found = False
        for i in range(len(A)):
            if found:
                break
            for j in range(len(A[0])):
                
                if A[i][j] == 1:
                    
                    visited = set()
                    
                    self.dfs(i, j, queue, A, visited)
                    found = True
                    break
        print(queue)
        
        step = 0
        while queue:
            for _ in range(len(queue)):
                cur_x, cur_y = queue.popleft()
                for dx, dy in Directions:
                    nx, ny = cur_x+dx, cur_y + dy
                    if not self.isValid(nx, ny, A) or (nx, ny) in visited:
                        continue
                    if A[nx][ny] == 1:
                        return step
                    queue.append((nx, ny))
                    visited.add((nx, ny))
            step += 1
        return -1
        
                
                
        
    
    def dfs(self, i, j, queue, A, visited):
        if A[i][j] == 0:
            return
        queue.append((i, j))
        visited.add((i, j))
        for dx, dy in Directions:
            nx, ny = i + dx, j + dy
            if not self.isValid(nx, ny, A) or (nx, ny) in visited:
                continue
            self.dfs(nx, ny, queue, A, visited)
    
    
    def isValid(self, x, y, A):
        return x >= 0 and x < len(A) and y >= 0 and y < len(A[0])
    
        

