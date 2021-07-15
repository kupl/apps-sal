class Unifindm:
    def __init__(self,n):
        self.arr = list(range(n))
        self.rank = [0]*n
    def union(self,a,b):
        a = self.find(a)
        b = self.find(b)
        
        if self.rank[a]<self.rank[b]:
            a,b = b,a
        
        if self.rank[a]==self.rank[b]:
            self.rank[a]+=1
        
        self.arr[b] = a
        
    def find(self,a):
        if self.arr[a]!=a:
            self.arr[a] = self.find(self.arr[a])
        return self.arr[a]

class Unifind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
    
    # make a and b part of the same component
    # union by rank optimization
    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        if pa == pb: return
        if self.rank[pa] > self.rank[pb]:
            self.parent[pb] = pa
            self.rank[pa] += self.rank[pb]
        else:
            self.parent[pa] = pb
            self.rank[pb] += self.rank[pa]
    
    # find the representative of the 
    # path compression optimization
    def find(self, a):
        if self.parent[a] == a:
            return a
        
        self.parent[a] = self.find(self.parent[a])
        return self.parent[a]
    
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        manhatan = lambda i,j : -(abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1]))
        edges = sorted((manhatan(i,j),i,j) for i in range(len(points)) for j in range(i+1,len(points)))
        #print(edges)
        uf = Unifind(len(points))
        count = 0
        cost = 0
        while count < len(points)-1:
            c,i,j = edges.pop()
            #if edge adds a cycle(both ends are already in)
            if uf.find(i)!=uf.find(j):
                cost-=c
                count+=1
                uf.union(i,j)
                
        #print(uf.arr)
        return cost
                
                

