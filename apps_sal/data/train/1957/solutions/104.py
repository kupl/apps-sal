class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[[False for _ in range(k+1)] for _ in range(n)] for _ in range(m)]
        # visited=[[False for _ in range(n)] for _ in range(m)]
        
       # k - grid[0][0] - grid[m-1][n-1] 是因为如果起点或者终点是obstacles, 那么需要预留出来一定的k来破坏obstacle        
        initialK = k - grid[0][0] - grid[m-1][n-1];
        
        # visited[0][0] = (True, initialK)
        
        if initialK < 0: 
            return -1
        visited[0][0][initialK] = True
        
        initial = ((0,0), initialK)
        queue = [initial]
        length = 0
        
        while queue:
            size = len(queue)
            length += 1
            for _ in range(size):
                node, kLeft = queue.pop(0)
                x,y = node
                # this is just for initial node is destination                
                if kLeft >= 0 and x == m-1 and y == n-1:
                    return length-1
                
                for direction in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nextX = x+direction[0]
                    nextY = y+direction[1]
        
                    if 0<=nextX<m and 0<=nextY<n:
                        nextKLeft = kLeft - grid[nextX][nextY]
                        if nextKLeft < 0 or visited[nextX][nextY][nextKLeft]:
                            #不符合条件, 或者visited过并且k还是同一个状态的可以剪枝
                            continue
                        else:
                            if nextX == m-1 and nextY == n-1:
                                return length
                            queue.append(((nextX, nextY), nextKLeft))
                            visited[nextX][nextY][nextKLeft] = True
                            
        return -1
                        
                            

