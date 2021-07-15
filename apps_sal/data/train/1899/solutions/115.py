from collections import deque
directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
# 先dfs， 再bfs。 
class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        n = len(A)
        m = len(A[0])
        visited = [[False] * m for _ in range(n)]
        q = deque([])
        found = False
        for i in range(n):
            if found:
                break
            for j in range(m):
                if A[i][j] == 1:
                    self.dfs(i, j, A, q, visited)
                    found = True
                    #这里要break。 如果不break会继续往下找，那么两个岛就连成一个了。 
                    break
        
        step = 0
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y+dy
                    if not self.isValid(nx, ny, A) or visited[nx][ny]:
                        continue
                    
                    if A[nx][ny] == 1:
                        return step
                    q.append((nx, ny))
                    visited[nx][ny] = True
                
            step += 1
        return -1
        
    def dfs(self,i, j, A, q, visited):
        if not self.isValid(i, j, A) or visited[i][j] or A[i][j] == 0:
            return
        visited[i][j] = True
        q.append((i, j))
        for dx, dy in directions:
            nx, ny = i+dx, j+dy
            # if not self.isValid(nx, ny, A) or visited[nx][ny]:
            #     continue
            self.dfs(nx, ny, A, q, visited)
        
    def isValid(self, i, j, A):
        return i >= 0 and i < len(A) and j >= 0 and j < len(A[0])
