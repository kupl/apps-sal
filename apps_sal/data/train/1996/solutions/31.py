class Solution:

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        flags = [0] * len(graph)

        def dfs(node, visited):
            visited.add(node)
            for neighbor in graph[node]:
                if flags[neighbor] == 1:
                    continue
                if flags[neighbor] == -1:
                    return False
                if neighbor in visited or not dfs(neighbor, visited.copy()):
                    flags[neighbor] = -1
                    return False
            flags[node] = 1
            return True
        visited = set()
        for i in range(len(graph)):
            if not flags[i]:
                dfs(i, visited)
        return [i for (i, flag) in enumerate(flags) if flag == 1]
