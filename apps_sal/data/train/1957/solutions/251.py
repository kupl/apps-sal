class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])
        
        if n == 1 and m == 1:
            if grid[0][0] == 0:
                return 0
            return -1 if k < 1 else 0
        
        visited = [[False] * m for i in range(n)]
        moves = [
            [0, 1],
            [1, 0],
            [-1, 0],
            [0, -1]
        ]
        
        q = []
        \"\"\"
        (x, y, k, steps)
        \"\"\"
        q.append((0, 0, k, 0))
        
        while len(q) != 0:
            curr = q.pop(0)
            
            if (curr[0], curr[1]) == (m - 1, n - 1):
                return curr[3]
            
            for move in moves:
                newX = curr[0] + move[0]
                newY = curr[1] + move[1]
                
                if newX >= m or newY >= n or newX < 0 or newY < 0:
                    continue
                
                if grid[newY][newX] == 1 and curr[2] == 0:
                    continue
                
                newK = curr[2] if grid[newY][newX] == 0 else curr[2] - 1
                if visited[newY][newX] != False:
                    old = visited[newY][newX]
                    if old[2] < newK:
                        newMove = (newX, newY, newK, curr[3] + 1)
                        q.append(newMove)
                        visited[newY][newX] = newMove
                else:
                    newMove = (newX, newY, newK, curr[3] + 1)
                    q.append(newMove)
                    visited[newY][newX] = newMove
        
        if not visited[n - 1][m - 1]:
            return -1
        return visited[n - 1][m - 1][3]
