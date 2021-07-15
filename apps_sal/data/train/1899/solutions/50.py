class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        
        self.A = A
        self.R = len(self.A)
        self.C = len(self.A[0])
        
        p = self.findGround()
        
        if p == None:
            return -1
        
        self.firstIsland = set()
        
        self.embraceIsland( p)

        return self.bfs()
    
    def findGround(self):
        for i in range(0, self.R):
            for j in range(0, self.C):
                if self.isGround((i, j)):
                    return (i, j)
                
        return None
    
    def isGround(self, p):
        return self.A[p[0]][p[1]] == 1
    
                
    def inGrid(self, p):
        
        if not (0 <= p[0] < self.R):
            return False
        
        if not (0 <= p[1] < self.C):
            return False
        
        return True
    
    def getNeis(self, p):
        neis = []
        
        neis.append((p[0] + 1, p[1]))
        neis.append((p[0] - 1, p[1]))
        neis.append((p[0], p[1] + 1))
        neis.append((p[0], p[1] - 1))
        
        return neis
    
    
    def embraceIsland(self, p):
        
        if p in self.firstIsland:
            return
        
        self.firstIsland.add(p)
        
        for nei in self.getNeis(p):
            if self.inGrid(nei) and self.isGround(nei) and nei not in self.firstIsland:
                self.embraceIsland(nei)
    
    def bfs(self):
        q = collections.deque()
        visited = set()
        
        for p in self.firstIsland:
            q.appendleft((p, 0))
            
        while q:
            node, dist = q.pop()
            
            if self.isGround(node) and node not in self.firstIsland:
                return dist - 1
            
            if node in visited:
                continue
                
            visited.add(node)
            
            for nei in self.getNeis(node):
                if self.inGrid(nei) and nei not in visited:
                    q.appendleft((nei, dist + 1))
        return -1
    

