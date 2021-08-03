
from collections import defaultdict

class Graph:
    def __init__(self):
        self.edges = defaultdict(list)
    def add_edge(self,src,dst,color):
        self.edges[src].append((dst,color))
        

class Solution:     
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        
        g = Graph()
        for src,dst in red_edges:
            g.add_edge(src,dst,\"R\")
        for src,dst in blue_edges:
            g.add_edge(src,dst,\"B\")
        
        
        data = [float(inf)]*(n)
        q = deque()
        q.append((0,0,None))
        visited = set()
        while(q):
            node,dist,prevColor = q.popleft()
            visited.add((node,prevColor))
            if(dist < data[node]):
                data[node] = dist
            
            for nei,col in g.edges[node]:
                if col!=prevColor and (nei,col) not in visited:
                    q.append((nei,dist+1,col))
        
        for i,e in enumerate(data):
            if e==float('inf'):
                data[i]=-1
        
        return data
                    
            
            
