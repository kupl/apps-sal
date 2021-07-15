\"\"\"
只有2个岛
先dfs - find 1st island's boundary nodes， label 1st island with 2
再bfs - expand 1st island's boundary, and mark unvisited 0 as prevstep+1, until finding 1
timeO(m*n) spaceO(m*n)
\"\"\"
class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        self.A = A
        boundaries = self.dfs()
        
        # bfs expand 1st island boundaries
        q = collections.deque([(i,j,self.A[i][j]) for i,j in boundaries]) # coordinate and step(+2)
        while q:
            i,j,step = q.popleft()
            for x,y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0<=x<len(self.A) and 0<=y<len(self.A[0]):
                    if self.A[x][y]==1: 
                        return step-2
                    elif self.A[x][y]==0:
                        self.A[x][y]=step+1
                        q.append((x,y,step+1))  
        return -1
    
    def getFist1(self): # find 1st island's starting 1
        for i in range(len(self.A)):
            for j in range(len(self.A[0])):
                if self.A[i][j] == 1:
                    return (i,j)
        return (-1,-1)
    
    def dfs(self): # find 1st island's boundaries; label visited to 2
        boundaries = set()
        stack = [self.getFist1()]
        while stack:
            i,j = stack.pop()
            self.A[i][j] = 2 # mark visited as 2
            for x,y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0<=x<len(self.A) and 0<=y<len(self.A[0]):
                    if self.A[x][y]==0: # i,j is boundary
                        boundaries.add((i,j))
                    elif self.A[x][y]==1: # i,j is in 1st island
                        stack.append((x,y))
        return boundaries
