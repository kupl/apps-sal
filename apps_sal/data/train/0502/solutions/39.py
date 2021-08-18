class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:

        sizeComponents = defaultdict(int)
        nodesToComponents = defaultdict(int)
        c = 0

        def dfs(node, c):
            sizeComponents[c] += 1
            nodesToComponents[node] = c
            for neighbor in range(len(graph[node])):
                if graph[node][neighbor] == 1 and node != neighbor:
                    if neighbor not in nodesToComponents:
                        dfs(neighbor, c)

        for node in range(len(graph)):
            if node not in nodesToComponents:
                dfs(node, c)
                c += 1

        initialComponents = defaultdict(int)
        for node in initial:
            component = nodesToComponents[node]
            initialComponents[component] += 1

        res = float('inf')
        for node in initial:
            component = nodesToComponents[node]
            size = sizeComponents[component]
            if initialComponents[component] == 1:
                if res == float('inf'):
                    res = node
                elif size > sizeComponents[nodesToComponents[res]]:
                    res = node
                elif size == sizeComponents[nodesToComponents[res]] and node < res:
                    res = node

        return res if res < float('inf') else min(initial)
