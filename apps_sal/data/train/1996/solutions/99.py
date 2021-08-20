def f(x, y, ci, v):
    a = True
    for i in x[ci]:
        if i in v:
            if y[i] != 1:
                a = False
            continue
        v.add(i)
        y[i] = f(x, y, i, v)
        a = y[i] and a
    return a


class Solution:

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        l = len(graph)
        y = [-1 for i in range(l)]
        v = set()
        for i in range(l):
            if y[i] == -1:
                v.add(i)
                y[i] = f(graph, y, i, v)
        return [i for i in range(l) if y[i]]
