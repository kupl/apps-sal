class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        parent = [x for x in range(n+1)]
        rank = [0]*(n+1)
        
        def find(x, parent):
            if x!=parent[x]:
                parent[x]=find(parent[x], parent)
            return parent[x]
        
        def union(x,y, parent, rank):
            xp, yp = find(x, parent), find(y, parent)
            if xp==yp:
                return False
            if rank[xp]>rank[yp]:
                parent[yp]=xp
            elif rank[xp]<rank[yp]:
                parent[xp]=yp
            else:
                parent[yp]=xp
                rank[xp]+=1
            return True
        
        type1 = [(u,v) for w,u,v in edges if w==1]
        type2 = [(u,v) for w,u,v in edges if w==2]
        type3 = [(u,v) for w,u,v in edges if w==3]
        
            
        ans = 0
        for u,v in type3:
            if not union(u,v, parent, rank):
                ans+=1
                
        p1 = parent.copy()
        r1 = rank.copy()
        
        for u,v in type1:
            if not union(u,v,p1,r1):
                ans+=1
                
        for u,v in type2:
            if not union(u,v,parent,rank):
                ans+=1
                
        arr1 = [find(p,p1) for p in p1[1:]]
        arr2 = [find(p,parent) for p in parent[1:]]
        if (arr1[1:] != arr1[:-1]) or (arr2[1:] != arr2[:-1]):
            return -1
        return ans
