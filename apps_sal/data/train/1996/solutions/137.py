class Solution:

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        (seen, safe) = (set(), set())

        def dfs(u):
            if u in seen:
                return u in safe
            seen.add(u)
            if all((dfs(v) for v in graph[u])):
                safe.add(u)
                return True
        return list(filter(lambda u: dfs(u), range(len(graph))))
