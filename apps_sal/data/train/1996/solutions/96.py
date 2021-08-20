class Solution:

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        (WHITE, GRAY, BLACK) = (0, 1, 2)
        color = collections.defaultdict(int)

        def dfs(node):
            if color[node] != WHITE:
                return color[node] == BLACK
            color[node] = GRAY
            for next_node in graph[node]:
                if color[next_node] == BLACK:
                    continue
                if color[next_node] == GRAY or not dfs(next_node):
                    return False
            color[node] = BLACK
            return True
        return filter(dfs, range(len(graph)))
