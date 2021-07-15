class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        A=[i+1 for i in range(n)]
        B=[i+1 for i in range(n)]
        cA=n
        cB=n
        edges.sort(reverse=True,key=lambda x:(x[0]))
        i=0
        m=len(edges)
        ans=0
        while i<m and edges[i][0]==3:
            l1=find(A,edges[i][1])
            l2=find(A,edges[i][2])
            if l1==l2:
                ans+=1
            else:
                #mi=min(l1,l2)
                #ma=max(l1,l2)
                A[l1-1]=-l2
                #print(l1,l2)
                #print(A)
                B[l1-1]=-l2
                cA-=1
                cB-=1
            if cA==1:
                return m-i-1+ans
            i+=1
        j=i
        while j<m and edges[j][0]==2:
            l1=find(B,edges[j][1])
            l2=find(B,edges[j][2])
            if l1==l2:
                ans+=1
            else:
                #mi=min(l1,l2)
                #ma=max(l1,l2)
                B[l1-1]=-l2
                cB-=1
            if cB==1:
                while j+1<m and edges[j+1][0]==2:
                    j+=1
                    ans+=1
                j+=1
                break
            else:
                j+=1
        if cB!=1:
            return -1
        while j<m:
            l1=find(A,edges[j][1])
            l2=find(A,edges[j][2])
            if l1==l2:
                ans+=1
            else:
                #mi=min(l1,l2)
                #ma=max(l1,l2)
                A[l1-1]=-l2
                cA-=1
            if cA==1:
                return m-j-1+ans
            j+=1
        
        return -1
        
            
            
            
def find(ll,x):
    if ll[x-1]>0:
        return ll[x-1]
    else:
        ll[x-1]=-find(ll,-ll[x-1])
        return(-ll[x-1])

