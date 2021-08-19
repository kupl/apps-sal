class Solution:

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        size = len(graph)
        AVAILABLE = 0
        VISITING = 1
        VISITED = 2
        status = [AVAILABLE] * size

        def isSafe(source, res):
            if status[source] != AVAILABLE:
                return status[source] == VISITED
            status[source] = VISITING
            for neighbour in graph[source]:
                if not isSafe(neighbour, res):
                    return False
            status[source] = VISITED
            res.append(source)
            return True
        res = []
        for node in range(size):
            isSafe(node, res)
        return sorted(res)
