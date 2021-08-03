class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        result = []
        outDegre = [0] * len(graph)
        for i in range(len(graph)):
            outDegre[i] = len(graph[i])
            if not outDegre[i]:
                result.append(i)
            for j in graph[i]:
                g[j].append(i)
        print(outDegre)
        for nodes in result:
            for nei in g[nodes]:
                outDegre[nei] = outDegre[nei] - 1
                if outDegre[nei] == 0:
                    result.append(nei)
        print(g)
        print(outDegre)
        return sorted(result)
