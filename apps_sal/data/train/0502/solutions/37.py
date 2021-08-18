class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        def method1():
            N = len(graph)
            colors = {}
            c = 0

            def dfs(node, color):
                colors[node] = color
                for nei, adj in enumerate(graph[node]):
                    if adj == 1 and nei not in colors:
                        dfs(nei, color)

            for node in range(N):
                if node not in colors:
                    dfs(node, c)
                    c += 1

            size = collections.Counter(colors.values())

            color_count = collections.Counter()
            for node in initial:
                color_count[colors[node]] += 1

            ans = float('inf')
            for initial_node in initial:
                c = colors[initial_node]
                if color_count[c] == 1:
                    if ans == float('inf'):
                        ans = initial_node
                    elif size[c] > size[colors[ans]]:
                        ans = initial_node
                    elif size[c] == size[colors[ans]] and initial_node < ans:
                        ans = initial_node

            return ans if ans < float('inf') else min(initial)

        def method2():
            def dfs(node, vis):
                for v in range(len(graph[node])):
                    if graph[node][v] == 1 and v not in vis:
                        vis.add(v)
                        dfs(v, vis)

            s = set(initial)
            seen = set()
            del_node, subgraph_len = min(initial), 0
            for node in range(len(graph)):
                if node not in seen:
                    vis = set([node])
                    dfs(node, vis)
                    infect = vis & s
                    if len(infect) == 1:
                        if len(vis) > subgraph_len or (len(vis) == subgraph_len and list(infect)[0] < del_node):
                            del_node, subgraph_len = list(infect)[0], len(vis)
                    seen |= vis
            return del_node

        return method2()
