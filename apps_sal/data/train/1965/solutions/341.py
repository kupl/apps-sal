class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        res, e0, e1 = 0, 0, 0
        self.root = [i for i in range(n+1)]
        def find(x):
            if x != self.root[x]:
                self.root[x] = find(self.root[x])
            return self.root[x]
        
        def uni(x, y):
            x, y = find(x), find(y)
            if x==y:
                return 1
            self.root[x] = y
            return 0
        
        for t,i,j in edges:
            if t == 3:
                if uni(i,j):
                    res += 1
                else:
                    e0 += 1
                    e1 += 1
                    
        root0 = self.root[:]
        for t,i,j in edges:
            if t == 1:
                if uni(i, j):
                    res += 1
                else:
                    e0 += 1
                    
        self.root = root0
        for t,i,j in edges:
            if t==2:
                if uni(i,j):
                    res += 1
                else:
                    e1 += 1
                    
        return res if e1 == e0 == (n-1) else -1
                    

