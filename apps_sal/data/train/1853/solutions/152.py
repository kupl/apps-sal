class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], d: int) -> int:
        if n==2:
            return 1
        
        graph = {x:[] for x in range(n)}
        for edge in edges:
            graph[edge[0]].append((edge[1],edge[2]))
            graph[edge[1]].append((edge[0],edge[2]))
        
        
        def reachable(node, visited, threshold, dist):
            for nei in graph[node]:
                if dist+nei[1]<visited[nei[0]] and dist+nei[1]<=threshold:
                    visited[nei[0]] = dist+nei[1] 
                    reachable(nei[0], visited, threshold, dist+nei[1])
                    
        res = 0
        temp = n
        for i in reversed(list(range(n))):
            visited = [float('inf') for _ in range(n)]
            visited[i] = 0
            c = 0
            dist = 0
            for nei in graph[i]:
                if dist+nei[1]<visited[nei[0]] and dist+nei[1]<=d:
                    visited[nei[0]] = dist+nei[1] 
                    reachable(nei[0], visited, d,dist+nei[1])
            
            for val in visited:
                if val>0 and val!=float('inf'):
                    c+=1
        
            print((c,i))
            if c < temp :
                res = i
                temp = c
        return res

