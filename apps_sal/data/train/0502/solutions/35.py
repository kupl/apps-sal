class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        colors = {}
        c = 0

        def dfs(node, graph, c):
            colors[node] = c
            for nei, adj in enumerate(graph[node]):
                if adj and nei not in colors:
                    dfs(nei, graph, c)
        # group into colors
        for i in range(len(graph)):
            if i not in colors:
                dfs(i, graph, c)
                c += 1
        size = collections.Counter(list(colors.values()))
        # group nodes from initial to have unique color
        init_count = collections.defaultdict(int)
        for node in initial:
            init_count[colors[node]] += 1
        # find ans
        ans = float('inf')
        for x in initial:
            if init_count[colors[x]] == 1:
                if ans == float('inf'):
                    ans = x
                elif size[colors[x]] > size[colors[ans]]:
                    ans = x
                elif size[colors[x]] == size[colors[ans]] and x < ans:
                    ans = x
        return ans if ans != float('inf') else min(initial)
