# dfs, with status: UNKNOWN, VISITING, VISITED
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        UNKNOWN, VISITING, VISITED = 0, 1, 2
        status = [UNKNOWN] * len(graph)

        def dfs(node):
            if status[node] == UNKNOWN:
                status[node] = VISITING
                if all([dfs(n) for n in graph[node]]):
                    status[node] = VISITED
                    return True
                else:
                    return False
            elif status[node] == VISITED:
                return True
            elif status[node] == VISITING:
                return False
        for n in range(len(graph)):
            if status[n] == UNKNOWN:
                dfs(n)
        return sorted([x for x, stat in enumerate(status) if stat == VISITED])
