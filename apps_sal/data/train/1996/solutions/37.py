class Solution:

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        color = [0] * len(graph)

        def df(v):
            if color[v] == 2:
                return True
            color[v] = 1
            for v2 in graph[v]:
                if color[v2] == 1 or (color[v2] == 0 and (not df(v2))):
                    return False
            color[v] = 2
            return True
        safe = []
        for v in range(len(graph)):
            if df(v):
                safe.append(v)
        return safe
