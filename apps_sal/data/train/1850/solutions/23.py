class Solution:

    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for (u, v) in edges:
            graph[u].append(v)
            graph[v].append(u)
        start = -1
        for node in graph:
            if len(graph[node]) == 1:
                start = node

        def getStartingDist(node, parent=None, d=0):
            return d + sum((getStartingDist(child, node, d + 1) for child in graph[node] if child != parent))
        dist = getStartingDist(start)
        remainingCt = {}

        def getCtRemaining(node, parent):
            remainingCt[node] = 1 + sum((getCtRemaining(child, node) for child in graph[node] if child != parent))
            return remainingCt[node]
        getCtRemaining(start, None)
        result = [None] * N
        result[start] = dist

        def dfs(node, parent, running, nodesUp):
            result[node] = running
            for child in graph[node]:
                if child != parent:
                    newNodesUp = nodesUp + remainingCt[node] - remainingCt[child]
                    newDistSum = running - (remainingCt[child] - 1) + (newNodesUp - 1)
                    dfs(child, node, newDistSum, newNodesUp)
        dfs(start, None, dist, 0)
        return result
