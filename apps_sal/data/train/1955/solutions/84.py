par=[0]*(100005)
rank=[1]*(100005)

def find(x):
    if par[x]!=x:
        par[x]=find(par[x])
    return par[x]
def union(x,y):
    xs = find(x)
    ys = find(y)
    if xs!=ys:
        if rank[xs]<rank[ys]:
            par[xs]=ys
        elif rank[xs]>rank[ys]:
            par[ys]=xs
        else:
            par[ys] = xs
            rank[xs]+=1
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        for i in range(n+3):
            rank[i]=1
            par[i]=i
        for i in pairs:
            union(i[0],i[1])
            #print(par[:5])
        #print(par[:10])
        poi=[0]*(n+3)
        #a=[0]*(n+3)
        for i in range(n):
            par[i]=find(par[i])
        ans=[[]for i in range(n+3)]
        for i in range(n):
            ans[par[i]].append(s[i])
        for i in range(n):
            ans[i].sort()
        fin=''
        for i in range(n):
            tmp = par[i]
            fin+=ans[tmp][poi[tmp]]
            poi[tmp]+=1
        return fin
            
        
        
        

