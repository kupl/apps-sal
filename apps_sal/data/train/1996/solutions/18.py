class Solution:

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        (W, G, B) = (0, 1, 2)
        color = collections.defaultdict(int)

        def dfs(node):
            if color[node] != W:
                return color[node] == B
            color[node] = G
            for nei in graph[node]:
                if color[nei] == B:
                    continue
                if color[nei] == G or not dfs(nei):
                    return False
            color[node] = B
            return True
        res = []
        for i in range(len(graph)):
            if dfs(i):
                res.append(i)
        return res
