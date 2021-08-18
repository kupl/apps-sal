from collections import defaultdict


class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        size = Counter()
        color = defaultdict(int)

        def dfs(node, c):
            color[node] = c
            size[c] += 1
            for nextNode, val in enumerate(graph[node]):
                if val and nextNode not in color:
                    dfs(nextNode, c)

        c = 0
        for node in range(len(graph)):
            if node not in color:
                dfs(node, c)
                c += 1

        color_count = Counter()
        for node in initial:
            color_count[color[node]] += 1

        ans = -1
        for node in initial:
            c = color[node]
            if color_count[c] == 1:
                if ans == -1:
                    ans = node
                elif size[c] > size[color[ans]]:
                    ans = node
                elif size[c] == size[color[ans]] and node < ans:
                    ans = node
        if ans == -1:
            return min(initial)
        return ans
