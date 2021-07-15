class Solution:
    def eventualSafeNodes(self, graph):
        degrees = {}
        safe, unsafe = set(), set()
        adj = {}
        for node in range(len(graph)):
            nodes = graph[node]
            degrees[node] = len(nodes)
            graph[node] = set(nodes)
            if node not in adj:
                adj[node] = set()
            for another in nodes:
                if another not in adj:
                    adj[another] = set()
                adj[another].add(node)
        queue = []
        for node in degrees:
            if degrees[node] == 0:
                queue.append(node)
        while True:
            if len(queue) == 0:
                break
            node = queue.pop()
            if degrees[node] == 0:
                safe.add(node)
                for another in adj[node]:
                    degrees[another] -= 1 
                    if degrees[another] == 0 and another not in safe:
                        queue.append(another)
            else:
                break
        safe = list(safe)
        safe.sort()
        return safe
                
                
                
                
        

                
            
                

