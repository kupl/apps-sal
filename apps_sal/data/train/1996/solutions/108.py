class Solution:

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        result = []
        indegree = [len(edge) for edge in graph]
        neighbors = collections.defaultdict(list)
        for (i, edge) in enumerate(graph):
            for j in edge:
                neighbors[j].append(i)
        queue = []
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        while queue:
            i = queue.pop(0)
            result.append(i)
            for neighbor in neighbors[i]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return sorted(result)
