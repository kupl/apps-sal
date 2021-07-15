class Solution:
    def span(self,A,n,flag,par):
        countt=0
        countu=0
        for i,(t,u,v) in enumerate(A):
            if t==flag:
                countt+=1
                p1=u
                while par[p1]>0:
                    p1=par[p1]
                p2=v
                while par[p2]>0:
                    p2=par[p2]
                    
                if p1==p2:
                    continue
                    
                else:
                    countu+=1
                    if abs(par[p1])>abs(par[p2]):
                        par[p1]-=par[p2]
                        if u!=p1:
                            par[u]=p1
                        par[v]=p1
                        par[p2]=p1
                    else:
                        par[p2]-=par[p1]
                        if v!=p2:
                            par[v]=p2
                        par[u]=p2
                        par[p1]=p2
         
        return countt,countu
        
    
    
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        edges.sort(key=lambda x:x[0],reverse=True)
        par=[-1]*(n+1)
        ct,cu=self.span(edges,n,3,par)
        if cu==n-1:
            return len(edges)-cu
        copy=par[:]
        ct2,cu2=self.span(edges,n,2,par)
        ct1,cu1=self.span(edges,n,1,copy)
        if cu+cu2!=n-1 or cu+cu1!=n-1:
            return -1
        
        return len(edges)-(cu+cu1+cu2)
        
        
        
        
        
        

