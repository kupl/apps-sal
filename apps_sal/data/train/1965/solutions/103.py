class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        
        size1 = [1] * n
        size2 = [1] * n
        par1 = [i for i in range(n)]
        par2 = [i for i in range(n)]
        distinct1 = [n]
        distinct2 = [n]
        
        def find(node, par):
            while par[node] != node:
                par[node] = par[par[node]]
                node = par[node]
            return node
        
        def union(a,b,size,par,distinct):
            root1 = find(a,par)
            root2 = find(b,par)
            
            if root1 != root2:
                if size[root1] < size[root2]:
                    par[root1] = par[root2]
                    size[root2] += size[root1]
                else:
                    par[root2] = par[root1]
                    size[root1] += size[root2]
                distinct[0]-=1
                return True
            return False
            
        edges.sort(key=lambda x:x[0],reverse=True)
        edges_needed = 0
        for i in edges:
            type = i[0]
            u = i[1]-1
            v = i[2]-1
            if type == 3:
                a = union(u,v,size1,par1,distinct1)
                b = union(u,v,size2,par2,distinct2)
                if a or b:
                    edges_needed+=1
            elif type == 1:
                if union(u,v,size1,par1,distinct1):
                    edges_needed+=1
            else:
                # print(u,v)
                if union(u,v,size2,par2,distinct2):
                    edges_needed+=1
                # print(par2)
        # print(par1,par2)        
        if distinct1[0] != 1 or distinct2[0] != 1:
            return -1
        return len(edges) - edges_needed
                
        
        

