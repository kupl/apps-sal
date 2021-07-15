class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
#         g = collections.defaultdict(list)
#         N = len(graph)
        
#         for i, end in enumerate(graph):
#             for x in end:
#                 g[i].append(x)
            
#         def dfs(node, cycle):
#             if(not g[node]):
#                 return True
            
#             c = False
#             for nei in g[node]:
#                 if(nei not in cycle):
#                     cycle.add(nei)
#                     if(not dfs(nei, cycle)):
#                         c = True
#                         break
#                     cycle.remove(nei)
#                 else:
#                     c = True
#                     break
#             if(not c):
#                 return True
#             else:
#                 return False
    
#         res = []
#         for i in range(N):
#             cycle = set()
#             cycle.add(i)
#             if(dfs(i, cycle)):
#                 res.append(i)
#         return res

        W, G, B = 0, 1, 2
        color = collections.defaultdict(int)
        
        def dfs(node):
            if(color[node] != W):
                return color[node] == B
            
            color[node] = G
            for nei in graph[node]:
                if(color[nei] == B):
                    continue
                if(color[nei] == G or not dfs(nei)):
                    return False
            color[node] = B
            return True
        
        res = []
        for i in range(len(graph)):
            if(dfs(i)):
                res.append(i)
        return res
