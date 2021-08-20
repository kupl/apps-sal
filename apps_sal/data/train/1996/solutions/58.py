class Solution:

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        v = [0] * n

        def circle(i):
            if v[i] == 2:
                return False
            if v[i] == 1:
                return True
            v[i] = 1
            for nei in graph[i]:
                if circle(nei):
                    return True
            v[i] = 2
            return False
        res = []
        for i in range(n):
            if circle(i):
                continue
            res.append(i)
        return res
