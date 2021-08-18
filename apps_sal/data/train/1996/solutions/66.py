class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        WHITE, GREY, BLACK = 0, 1, 2
        result = []

        color = defaultdict()
        for i in range(len(graph)):
            color[i] = WHITE

        def dfs(node):
            if color[node] != WHITE:
                return color[node] == BLACK

            color[node] = GREY
            for neigh in graph[node]:
                if not dfs(neigh):
                    return False

            color[node] = BLACK
            return True

        for i in range(len(graph)):
            if not graph[i]:
                result.append(i)
            elif dfs(i):
                result.append(i)

        return result
