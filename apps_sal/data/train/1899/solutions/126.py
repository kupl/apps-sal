class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        R, C = len(A), len(A[0])
        
        def neighbors(r, c):
            for cr, cc in [(r+1,c),(r,c-1), (r-1,c), (r,c+1)]:
                if 0 <=cr<R and 0<=cc<C:
                    yield cr, cc
        
        def get_connections():
            connections = []
            done = set()
            for r, row in enumerate(A):
                for c, val in enumerate(row):
                    if val and (r,c) not in done:
                        print(\"r : \", r, \"c : \", c)
                        #Start DFS
                        stack = [(r,c)]
                        seen = {(r,c)}
                        while stack:
                            node = stack.pop()
                            for nei in neighbors(*node):
                                if A[nei[0]][nei[1]] and nei not in seen:
                                    stack.append(nei)
                                    seen.add(nei)                           
                        done |= seen                 
                        connections.append(seen)
                                             
            return connections
                                             
            
        source, target = get_connections()
        done = set(source)                      
        queue = collections.deque([(node,0) for node in source])
        while queue:
            #BFS
            node, d = queue.popleft()
            if node in target:
                return d-1
            for nei in neighbors(*node):
                if nei not in done:
                    queue.append((nei, d+1))
                    done.add(nei)
                    
                                             
                                             
