from collections import defaultdict


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        def dfs(node, group, groups):
            if node not in groups:
                groups[node] = group
            elif group != groups[node]:
                return True
            elif group == groups[node]:
                return False

            for next_node in graph[node]:
                fail = dfs(next_node, not groups[node], groups)
                if fail == True:
                    return True

            return False

        graph = defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        groups = {}

        for node in graph:
            if node not in groups:
                fail = dfs(node, True, groups)
                if fail:
                    return False

        return True
