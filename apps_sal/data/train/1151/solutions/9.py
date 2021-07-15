from collections import defaultdict 
def dfs(node):
    visit[node]=True
    nonlocal flag
    flag=1
    for i in g[node]:
        if visit[i]==False:
            dfs(i)

for _ in range(int(input())):
    n,m=list(map(int,input().split()))
    g = defaultdict(list)
    for i in range(m):
        u,v=list(map(int,input().split()))
        g[u].append(v)
        g[v].append(u)
    flag=0
    c=0
    visit=[False]*(n+1)
    for i in range(0,n):
        if visit[i]==False:
            flag=0
            dfs(i)
            if flag==1:
                c+=1
    print(c)
        
    

