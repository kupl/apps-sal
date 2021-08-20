class Solution:

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        def dfs(node, graph):
            nodes[node] = 1
            for child in graph[node]:
                if nodes[child] == 1:
                    return False
                if not nodes[child] and (not dfs(child, graph)):
                    return False
            nodes[node] = 2
            return True
        nodes = [0 for _ in range(len(graph))]
        ans = []
        for node in range(len(graph)):
            if dfs(node, graph):
                ans.append(node)
        return ans
