class Solution:
    
    def bfs(self, graph, src, num_nodes, threshold):
        
        d = [float('inf')] * num_nodes
        q = []
        
        q.append(src)
        d[src] = 0
        
        while len(q) > 0:
            u = q.pop(0)
            #print('Exploring edges of u = ', u)
            for v in graph[u]:
                #print(v)
                if d[v[0]] > d[u] + v[1]:
                    d[v[0]] = d[u] + v[1]
                    q.append(v[0])
        #print(d)
        return len([i for i,x in enumerate(d) if x <= threshold and x != 0])
                    
                
        
        
    
    
    
    
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        # form a graph
        
        graph = collections.defaultdict(list)
        
        for e in edges:
            graph[e[0]].append([e[1], e[2]])
            graph[e[1]].append([e[0], e[2]])
        
        #print(self.bfs(graph, 4, n, distanceThreshold))
        
        min_val = float('inf')
        node = -1
        for i in range(n):
            r = self.bfs(graph, i, n, distanceThreshold)
            if r <= min_val:
                node = i
                min_val = r
                
        return node
                
            
        
        
        

