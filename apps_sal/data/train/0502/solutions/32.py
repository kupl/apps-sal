class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        def dfs(node,vis):
            for v in  range(len(graph[node])):
                if graph[node][v] == 1 and v not in vis:
                    vis.add(v)
                    dfs(v,vis)

        s = set(initial)
        t_vis = set()
        del_node, subgraph_len = min(initial), 0
        for node in range(len(graph)):
            if node not in t_vis:
                vis = set([node])
                dfs(node,vis)
                # caculate the number of infected node in the subgraph
                infect = vis & s
                if len(infect) == 1:
                    # more number of nodes or smaller index
                    if len(vis) > subgraph_len or (len(vis) == subgraph_len and list(infect)[0] < del_node):
                        del_node,subgraph_len = list(infect)[0],len(vis)
                t_vis |= vis
        return del_node
#         def find(x):
#             if x != parents[x]:
#                 parents[x] = find(parents[x])
#             return parents[x]
        
#         def union(x, y):
#             parents[find(x)] = find(y)
            
#         n = len(graph)
#         parents = list(range(n))
#         for i in range(n):
#             for j in range(i + 1, n):
#                 if graph[i][j] == 1:
#                     union(i, j)
                    
#         union = collections.Counter(find(i) for i in range(n))
#         print(union)
#         malware = collections.Counter(find(i) for i in initial)
#         print(malware)
        
#         save, res = 0, min(initial)
#         for i in initial:
#             if malware[find(i)] == 1:
#                 if union[find(i)] > save:
#                     save, res = union[find(i)], i
#                 elif union[find(i)] == save:
#                     res = min(res, i)
#         return res
        
#         # return min(initial, key=lambda x: [(malware[find(x)] == 1) * -union[find(x)], x])
                    
        

