class Solution:

    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:

        def dfs(node, vis):
            for v in range(len(graph[node])):
                if graph[node][v] == 1 and v not in vis:
                    vis.add(v)
                    dfs(v, vis)
        s = set(initial)
        t_vis = set()
        (del_node, subgraph_len) = (min(initial), 0)
        for node in range(len(graph)):
            if node not in t_vis:
                vis = set([node])
                dfs(node, vis)
                infect = vis & s
                if len(infect) == 1:
                    if len(vis) > subgraph_len or (len(vis) == subgraph_len and list(infect)[0] < del_node):
                        (del_node, subgraph_len) = (list(infect)[0], len(vis))
                t_vis |= vis
        return del_node
