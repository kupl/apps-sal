from collections import defaultdict
 
class Graph:
 
    def __init__(self,vertices):
 
        self.graph = defaultdict(list)
        self.DFSList = defaultdict(list)
        
        for i in range(0,vertices):
        	self.graph[i]=[]
        	self.DFSList[i]=[]
 	

    def addEdge(self,u,v):
        if u!=v:
        	self.graph[u].append(v)
        	self.graph[v].append(u)
        	
    def DFSUtil(self,v,visited,n):
 
        visited[v]= True
        self.DFSList[n].append(v)
       
        
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited,n)
 
    def DFS(self,v):
 
        visited = [False]*(len(self.graph))
        self.DFSUtil(v,visited,v)
 
t=int(input())
for z in range(0,t):
	n,m=map(int,input().split())
	g = Graph(n)

	for M in range(0, m):
		u,v = map(int,input().split())
		g.addEdge(u,v)
	
	for i in range(0,n):
		g.DFS(i)
		
	q = int(input())
	for Q in range(0, q):
		u,v = map(int,input().split())
		if v in g.DFSList[u]:
			print("YO")
		else:
			print("NO")

