class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        #coloring each component (belong to different connected components)
        #count the size of each color
        #find unique nodes in initial
        #for each node with a unique color, choose the largest size, if there is a tie, choose the one with the smaller index
        N = len(graph)
        colors = {}# colors[node] = the color of this node.
        c = 0
        def dfs(node, color):
            colors[node] = color
            for nei, adj in enumerate(graph[node]):
                if adj and nei not in colors:#nei in colors的情况都考虑过了
                    dfs(nei, color)
        for node in range(N):
            if node not in colors:
                dfs(node, c)
                c += 1
        size = collections.Counter(list(colors.values()))# size[color] = number of occurrences of this color.
        color_count = collections.Counter()
        for node in initial:
            color_count[colors[node]] += 1
        ans = -1# the index of node to be removed
        for x in initial:
            if color_count[colors[x]] == 1:
                if ans == -1:
                    ans = x
                elif size[colors[x]] > size[colors[ans]]:
                    ans = x
                elif size[colors[x]] == size[colors[ans]] and x < ans:
                    ans = x
        return ans if ans != -1 else min(initial)#why we need to remove the minimum of initial, it won't reduce the malware count

