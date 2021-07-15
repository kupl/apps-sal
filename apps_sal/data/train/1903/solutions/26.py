class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        if n==1:
            return 0
        heap=[]
        dsu=DisjointSetUnion(n)
        for i in range(n-1):
            for j in range(i+1,n):
                distance=abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                heappush(heap,(distance,i,j))
        ans=0
        while heap:
            distance,i,j=heappop(heap)
            if dsu.find(i)!=dsu.find(j):
                ans += distance
                dsu.union(i,j)
        return ans
            
class DisjointSetUnion(object):

    def __init__(self, size):
        # initially, each node is an independent component
        self.parent = [i for i in range(size+1)]
        # keep the size of each component
        self.size = [1] * (size+1)
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        
        # the two nodes share the same set
        if px == py:
            return px
        
        # otherwise, connect the two sets (components)
        if self.size[px] > self.size[py]:
            # add the node to the union with less members.
            # keeping px as the index of the smaller component
            px, py = py, px
        # add the smaller component to the larger one
        self.parent[px] = py
        self.size[py] += self.size[px]
        # return the final (merged) group
        return py          
