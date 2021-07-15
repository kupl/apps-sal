class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = set()
        revg = defaultdict(set)
        q = deque()
        
        graph = list(map(set,graph))
        
        for u,nodes in enumerate(graph):
            if not nodes:
                q.append(u)
            for v in nodes:
                revg[v].add(u)
                
        while q:
            temp = q.popleft()
            safe.add(temp)
            for v in revg[temp]:
                graph[v].remove(temp)
                if not graph[v]:
                    q.append(v)
                    
        return sorted(safe)
