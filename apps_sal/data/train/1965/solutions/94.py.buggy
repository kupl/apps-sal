
class dsu:
    def __init__(self,n):
        self.parent =[-1 for i in range(n)]
        self.size = [0 for i in range(n)]

    def make_set(self,node):
        self.parent[node] = node

    def find(self,a):
        if self.parent[a] == a:
            return self.parent[a]
        else:
            self.parent[a] = self.find(self.parent[a])
            return self.parent[a]

    def union(self,a,b):
        a = self.find(a)
        b = self.find(b)
        if a!=b:
            if self.size[a] < self.size[b]:
                temp = a
                a = b
                b = temp
            self.parent[b] =self.parent[a]
            self.size[a] = self.size[a] + self.size[b]

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        
        ans = 0
        treeA = dsu(n+1)
        treeB = dsu(n+1)
        for i in range(n+1):
            treeA.make_set(i)
            treeB.make_set(i)
        edges.sort(reverse = True)
        # print(edges)
        m = len(edges)
        i = 0
        while(i<m and edges[i][0]==3):
            if treeA.find(edges[i][1]) == treeA.find(edges[i][2]) :
                ans= ans + 1
                i= i +1
                continue
            
            treeA.union(edges[i][1],edges[i][2])
            treeB.union(edges[i][1],edges[i][2])
            i= i +1
        # print(treeB.parent,\"B\")
        # print(treeA.parent,\"A\")
        while(i<m and edges[i][0]==2):
            if treeA.find(edges[i][1]) == treeA.find(edges[i][2]) :
                ans= ans + 1
                i= i +1
                continue
            treeA.union(edges[i][1],edges[i][2])
            # print(treeA.parent,\"A\")
            i= i +1
            
        while(i<m and edges[i][0]==1):
            if treeB.find(edges[i][1]) == treeB.find(edges[i][2]) :
                ans= ans + 1
                print(\"here\")
                i= i +1
                continue
            treeB.union(edges[i][1],edges[i][2])
            # print(treeB.parent,\"B\",ans,edges[i])
            i= i +1
        def check(tree):
            curr= tree.find(1)
            for i in range(1,n+1):
                if tree.find(i) != curr:
                    return 0
            return 1
        # print(ans)
        if check(treeA) == 0 or check(treeB) == 0:
            return -1
        return ans
                
        
        
