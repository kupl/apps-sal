import queue 
from collections import defaultdict
class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        q = queue.Queue()
        graph = defaultdict(list)
        degree = [0] * (n+1)
        for f, end in edges:
            graph[f].append(end)
            graph[end].append(f)
            degree[end] += 1
        start = 1
        # for ind, val in enumerate(degree):
        #     if val == 0:
        #         start = ind 
        visited = set()
        
        q.put([start, 1, 1]) # node, level (t is # of level), prob
        visited.add(start)
        res = 0 
        qt = 0
        
        p = [0] * (n+1)
        p[1] = 1.0
        while t and not q.empty():
            qsize = q.qsize()
            for _ in range(qsize):
                node, level, prob = q.get()
                size = 0
                for nei in graph[node]:
                    if nei not in visited:
                        size += 1
                for nei in graph[node]:
                    if nei not in visited:
                        visited.add(nei)
                        q.put([nei, level+1, prob*(1/size)])
                        p[nei] = p[node]/size
                if size > 0:
                    p[node] = 0 
            t -= 1
        return p[target]
