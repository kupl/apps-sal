class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        def dfs(node, vis):
            for connect in range(len(graph[node])):
                if graph[node][connect] == 1 and connect not in vis:
                    vis.add(connect)
                    dfs(connect, vis)
                    
        init = set(initial)
        total_vis = set()
        del_node, subgraph_len = min(initial), 0
        for node in range(len(graph)):
            if node not in total_vis:
                vis = set([node])
                dfs(node, vis)
                infect = vis & init
                if len(infect) == 1:
                    if len(vis) > subgraph_len or (len(vis) == subgraph_len and list(infect)[0] < del_node):
                        del_node, subgraph_len = list(infect)[0], len(vis)
                total_vis |= vis
        return del_node
