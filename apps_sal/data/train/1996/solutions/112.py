class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        def cycle(ind):
            if color[ind] == 1:
                return True
            if color[ind] == 2:
                return False

            color[ind] = 1

            for node in graph[ind]:
                if cycle(node):
                    return True
            color[ind] = 2
            return False

        n = len(graph)
        color = [0] * n

        for i in range(len(graph)):
            cycle(i)

        return [i for i in range(n) if color[i] == 2]
