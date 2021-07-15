from collections import defaultdict, deque
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        degree = [len(graph[i]) for i in range(len(graph))]
        edges = defaultdict(list)
        for i in range(len(graph)):
            for j in graph[i]:
                edges[j].append(i)
        
        q = deque()
        for i in range(len(graph)):
            if degree[i] == 0:
                q.append(i)
        
        res = []
        while q:
            node = q.popleft()
            res.append(node)
            for n in edges[node]:
                degree[n] -= 1
                if degree[n] == 0:
                    q.append(n)
        return sorted(res)
