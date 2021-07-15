from collections import *
for _ in range(int(input())):
    graph=defaultdict(list)
    def edge(x,y):
        graph[x].append(y)
    def deltafun(s,visited):
        visited[s]=1
        for i in graph[s]:
            if visited[i]==0:
                deltafun(i,visited)
        
    def delta(s):
        visited=[0]*n
        ans=0
        for i in range(n):
            if visited[i]==0:
                deltafun(i,visited)
                ans+=1
        return ans        
        
    n,m=list(map(int,input().split()))
    for i in range(m):
        a,b=list(map(int,input().split()))
        edge(a,b)
        edge(b,a)
    print(delta(0))    

