class Solution:

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        def cycle(snode):
            if mem[snode] == -1:
                return True
            elif mem[snode] == 1:
                return False
            mem[snode] = -1
            for e in graph[snode]:
                if cycle(e):
                    return True
            mem[snode] = 1
            return False
        n = len(graph)
        ret = []
        mem = [0] * n
        for i in range(n):
            if not cycle(i):
                ret.append(i)
        return ret
