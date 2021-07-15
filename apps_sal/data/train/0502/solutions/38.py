class DSU():
    
    def __init__(self):
        self.parent={}
        self.size={}
    
    def find(self,x):
        if x!=self.parent[x]:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        xp,yp=self.find(x),self.find(y)
        if xp==yp:
            return False
        if self.size[xp]<self.size[yp]:
            xp,yp=yp,xp
        
        self.size[xp]+=self.size[yp]
        self.parent[yp]=xp
        return True

    def add_node(self,x):
        self.parent[x]=x
        self.size[x]=1


class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        initial.sort()
        edges=[]
        for i in range(len(graph)):
            for j in range(i+1,len(graph[0])):
                if graph[i][j]:edges.append([i,j])
        
        dsu=DSU()
        for i in range(len(graph)):
            dsu.add_node(i)
            
        for e1,e2 in edges:
            if e1!=e2: dsu.union(e1,e2)
        ans=initial[0]
        m=len(graph)+1
        for i in initial:
            
            mt=self.get_max_size(initial,dsu,i)
            if mt<m:
                m=mt
                ans=i
        return ans
        
    
    def get_max_size(self,initial,dsu,di):
        x=0
        parents=set([])
        for i in initial:
            if i!=di:
                parents.add(dsu.find(i))
        
        for n in dsu.parent:
            if dsu.find(n) in parents:
                x+=1
        return x
        
        
            
        

