import sys

def find(u,a):
    if a[u]!=-1:
         a[u]=find(a[u],a)
         return a[u]
    else:
        return u
def union(a,u,v,ct):
    x=find(u,a)
    y=find(v,a)
    #print(x,y)
    if x==y:
        ct+=1
    else:
        a[x]=y
        ct=ct
    return ct    
        
n,k=map(int,input().split())
a=[-1 for i in range(n+1)]
count=0
for i in range(k):
    u,v=map(int,input().split())
    count=union(a,u,v,count)
    #print(a)
    
print(count)
