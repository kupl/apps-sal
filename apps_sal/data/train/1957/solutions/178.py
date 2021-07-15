from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        def valid(i,j):
            if i>=0 and j>=0 and i<len(grid) and j<len(grid[0]):
                return True
            return False
        
        dq=deque([(0,0,k,0)])
        visited=set()
        res=math.inf
        
        def search(i,j,k,l):
            if (i,j,k) in visited:
                return False
            nonlocal res
            if k<0:
                return False
            if i==len(grid)-1 and j==len(grid[0])-1:
                res=l
                return True
            for di,dj in [(1,0),(0,1),(-1,0),(0,-1)]:
                if valid(i+di,j+dj):
                    next_k=k if grid[i+di][j+dj]==0 else k-1
                    dq.append((i+di,j+dj,next_k,l+1))
            visited.add((i,j,k))
            return False
        while dq:
            i,j,k,l=dq.popleft()
            if search(i,j,k,l):
                break
        return res if res!=math.inf else -1

