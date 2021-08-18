
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = collections.defaultdict(set)
        for u, v in dislikes:
            graph[u].add(v)
            graph[v].add(u)

        group_map = {}

        def dfs(node, is_one):
            if node in group_map:
                return is_one == group_map[node]
            else:
                group_map[node] = is_one
            return all(dfs(nei, not is_one) for nei in graph[node])

        return all(dfs(node, True) for node in range(1, N + 1) if node not in group_map)
