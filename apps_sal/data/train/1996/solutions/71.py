class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        deg = {}
        grev = {}
        terminals = []
        for i in range(n):
            deg[i] = len(graph[i])
            if deg[i] == 0:
                terminals.append(i)
            for j in graph[i]:
                if j not in grev:
                    grev[j] = []
                grev[j].append(i)
        for t in terminals:
            if t not in grev:
                continue
            for j in grev[t]:
                deg[j] -= 1
                if deg[j] == 0:
                    terminals.append(j)
        return sorted(terminals)
