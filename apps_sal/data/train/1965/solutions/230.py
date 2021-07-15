class DSU:
    def __init__(self,n):
        self.node = list(range(n+1))
        self.rank = [1]*(n+1)
    
    def find(self,x):
        if self.node[x] != x:
            self.node[x] = self.find( self.node[x] )
        return self.node[x]
    
    def union(self,x,y):
        xid, yid = self.find(x), self.find(y)
        if xid == yid:
            return False
        else:
            xrank = self.rank[xid]
            yrank = self.rank[yid]
            if xrank<= yrank:
                self.node[xid] = yid
                self.rank[yid] += xrank
            else:
                self.node[yid] = xid
                self.rank[xid] += yrank
            return True

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice = []
        bob = []
        both = []
        for t,u,v in edges:
            if t==1:
                alice.append([u,v])
            elif t==2:
                bob.append([u,v])
            elif t==3:
                both.append([u,v])
        adsu = DSU(n)
        bdsu = DSU(n)
        ans = 0
        for u,v in both:
            T1 =  adsu.union(u,v) 
            T2 =  bdsu.union(u,v)
            if not T1 and not T2:
                ans += 1
        for u,v in alice:
            if not adsu.union(u,v):
                ans += 1
        for u,v in bob:
            if not bdsu.union(u,v):
                ans += 1
        for i in range(n+1):
            adsu.find(i)
            bdsu.find(i)
        return ans if len(set(adsu.node))==2 and len(set(bdsu.node))==2 else -1
                
        
        
        
        


