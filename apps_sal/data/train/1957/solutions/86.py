class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        queue = collections.deque([(0,0,k,0)])
        h = len(grid)
        if h==0:
            return 0
        w = len(grid[0])
        visited = set()
        while len(queue) > 0:
            i,j,k_left,step = queue.popleft()
            if i<0 or j<0 or i>=h or j>=w: # in valid
                continue
            if grid[i][j] == 1:
                k_left -= 1    
            # print(i,j,k_left)
            if k_left < 0 or (i,j,k_left) in visited:
                continue
            
            visited.add((i,j,k_left))
            # print(\"visit\",i,j,\"   k\",k_left,\"step\",step)

            if i == h-1 and j== w-1:
                return step
            
            queue.append((i+1,j,k_left,step+1))
            queue.append((i-1,j,k_left,step+1))
            queue.append((i,j+1,k_left,step+1))
            queue.append((i,j-1,k_left,step+1))
                
        return -1
        
        
        

