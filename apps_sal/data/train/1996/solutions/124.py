import collections


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        WHITE, GRAY, BLACK = 0, 1, 2
        color_of_nodes = collections.defaultdict(int)

        def dfs(node):
            if color_of_nodes[node] != WHITE:
                return color_of_nodes[node] == BLACK

            color_of_nodes[node] = GRAY
            for nei in graph[node]:
                if color_of_nodes[nei] == GRAY or not dfs(nei):
                    return False
            color_of_nodes[node] = BLACK
            return True

        res = []
        for i, node in enumerate(graph):
            if dfs(i):
                res.append(i)
        return res
