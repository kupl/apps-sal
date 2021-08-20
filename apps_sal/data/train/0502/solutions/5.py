class Solution:

    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        if len(graph) == 0:
            return 0
        g = dict()
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                if graph[i][j]:
                    if i in g:
                        g[i].append(j)
                    else:
                        g[i] = [j]
        groups = []
        initialSet = set(initial)
        numOfNodes = [0] * len(graph)
        for (v, e) in list(g.items()):
            if v not in initialSet:
                continue
            num = 1
            initialSet.remove(v)
            group = [v]
            stack = e
            visited = {v}
            while len(stack) != 0:
                vertex = stack.pop()
                if vertex not in visited:
                    if vertex in initialSet:
                        initialSet.remove(vertex)
                        group.append(vertex)
                    stack.extend(g[vertex])
                    visited.add(vertex)
                    num += 1
            groups.append(group)
            numOfNodes[v] = num
        canRemove = set([group[0] for group in groups if len(group) == 1])
        if len(canRemove) == 0:
            return min(initial)
        result = -1
        for vertex in initial:
            if vertex in canRemove and (result == -1 or numOfNodes[vertex] > numOfNodes[result]):
                result = vertex
            elif vertex in canRemove and numOfNodes[vertex] == numOfNodes[result] and (vertex < result):
                result = vertex
        return result
