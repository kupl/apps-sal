class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        WHITE, GREY, BLACK = 0, 1, 2
        color = collections.defaultdict(int)

        def dfs(u):
            if color[u] != WHITE:
                return color[u] != GREY

            color[u] = GREY
            for v in graph[u]:
                if color[v] == BLACK:
                    continue
                if color[v] == GREY or not dfs(v):
                    return False

            color[u] = BLACK

            return True

        return list(filter(dfs, range(len(graph))))
