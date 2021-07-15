class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # BFS
        safe = [False] * len(graph)
        rev = [set() for _ in range(len(graph))]
        queue = collections.deque()
        
        for i, nodes in enumerate(graph):
            if not nodes:
                queue.append(i)
            else:
                for node in nodes:
                    rev[node].add(i)
        
        while queue:
            curr = queue.popleft()
            safe[curr] = True
            for j in rev[curr]:
                graph[j].remove(curr)
                if len(graph[j]) == 0:
                    queue.append(j)
        return [i for i, val in enumerate(safe) if val]
        
        
        # DFS
#         W, G, B = 0, 1, 2     # gray: entry; black: exit
#         color = collections.defaultdict(int)
        
#         def dfs(node):
#             if color[node] == G:
#                 return False
#             if color[node] == B:
#                 return True
            
#             color[node] = G
#             for nei in graph[node]:
#                 if color[nei] == B:
#                     continue
#                 if color[nei] == G or not dfs(nei):
#                     return False
                
#             color[node] = B
#             return True
            
        
#         res = []
#         for i in range(len(graph)):
#             if dfs(i): res.append(i)
#         return res

