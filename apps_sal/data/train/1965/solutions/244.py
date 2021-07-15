class DSU:
    def __init__(self, n):
        self.p = list(range(n + 1))
        self.isolated_nodes = n
        
    def find(self, x):
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    
    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        
        if xr != yr:
            self.isolated_nodes -= 1
            
        self.p[xr] = yr

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        #keep two union for Bob and Alice
        #add edges to the dsu, if the two nodes are already in a union, we can delete the edge
        #always add type3 first
        edges.sort(reverse = True)
        
        dsuA = DSU(n)
        dsuB = DSU(n)
        res = 0
        for [t, n1, n2] in edges:
            if t == 3:
                #handle Alice
                if dsuA.find(n1) == dsuA.find(n2) and dsuB.find(n1) == dsuB.find(n2):
                    #don't add the edge
                    res += 1
                else:
                    dsuA.union(n1, n2)
                    dsuB.union(n1, n2)
            elif t == 1:
                #Alice
                if dsuA.find(n1) == dsuA.find(n2):
                    res += 1
                else:
                    dsuA.union(n1, n2)
            else:
                if dsuB.find(n1) == dsuB.find(n2):
                    res += 1
                else:
                    dsuB.union(n1, n2)
                    
        return res if dsuA.isolated_nodes == 1 and dsuB.isolated_nodes == 1 else -1
                

