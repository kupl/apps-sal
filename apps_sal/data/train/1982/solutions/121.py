import queue

def bfs_step(queue, colors, graph, queued):
    node = queue.get()
    color1 = colors[node]
    for edge in graph[node]:
        if colors[edge] == -1:
            colors[edge] = 1 - color1
        if colors[edge] == color1:
            return False
        if not queued[edge]:
            queue.put(edge)
            queued[edge] = 1
    return True

class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        q = queue.SimpleQueue()
        colors = [-1 for i in range(N+1)]
        graph = [[] for i in range(N+1)]
        queued = [0 for i in range(N+1)]
        for edge in dislikes:
            i, j = edge
            graph[i].append(j)
            graph[j].append(i)
        for i in range(N):
            if colors[i] != -1:
                continue
            colors[i] = 1
            if not queued[i]:
                q.put(i)
                queued[i] = 1
            while not q.empty():
                if not bfs_step(q, colors, graph, queued):
                    return False
        return True
                
                
            
        
            

