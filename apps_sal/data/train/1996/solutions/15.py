class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited = [False for i in range(len(graph))]
        recStack = [False for i in range(len(graph))]

        def dfs(node):
            visited[node] = True
            recStack[node] = True
            for nbor in graph[node]:
                if not visited[nbor]:
                    if dfs(nbor):
                        return True
                elif recStack[nbor]:
                    return True

            recStack[node] = False
            return False

        res = []
        for vert in range(len(graph)):
            if not dfs(vert):
                res.append(vert)
        res.sort()
        return res
