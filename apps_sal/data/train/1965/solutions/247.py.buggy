class unionFindSet:
    def __init__(self, S):
        self.parent = {i:i for i in S}
        self.rank = {i:1 for i in S}
        self.count = len(S) #number of groups
        
    def find(self, u):
        if u not in self.parent:
            return -1
        path = []
        while self.parent[u]!=u:
            path.append(u)
            u = self.parent[u]
        for p in path: #make tree flat
          \tself.parent[p] = u
        return u
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu==pv:
            return False
        if self.rank[pu] > self.rank[pv]: #union by rank
            pu, pv = pv, pu
        self.parent[pu] = pv #pu not u !!!
        self.rank[pv] += 1
        self.count -= 1
        return True

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        #edges = set([tuple(i) for i in edges])
        data = unionFindSet([i for i in range(1, n + 1)])
        e1, e2, res = 0, 0, 0
        edges3 = [(t, u, v) for t, u, v in edges if t==3] 
        edges1 = [(t, u, v) for t, u, v in edges if t==1] 
        edges2 = [(t, u, v) for t, u, v in edges if t==2]
        ## 2 + 3
        for i in range(len(edges3)):
            t, u, v = edges3[i]
            if data.find(u) != data.find(v):
                data.union(u, v)
                e1 += 1
                e2 += 1
            else:
                res += 1
        data2 = copy.deepcopy(data) ##########
        
        for i in range(len(edges2)):
            t, u, v = edges2[i]
            if data.find(u) != data.find(v):
                data.union(u, v)
                e2 += 1
            else:
                res += 1
        if data.count != 1:
            return -1
        
        ## 2 + 3
        for i in range(len(edges1)):
            t, u, v = edges1[i]
            if data2.find(u) != data2.find(v):
                data2.union(u, v)
                e1 += 1
            else:
                res += 1
        if data2.count != 1:
            return -1

        return res
    #先 uf 公共边然后存起来 然后分别对 alice 和 bob 做一下


                
            
            
        
        
        
        
