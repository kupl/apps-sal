class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        def dfs(node, graph):
            nodes[node] = 1  # mark as visiting
            for child in graph[node]:
                if nodes[child] == 1:
                    return False
                if not nodes[child] and not dfs(child, graph):
                    return False
            nodes[node] = 2
            return True

        nodes = [0 for _ in range(len(graph))]
        ans = []
        # check if there is a cycle at each node in the graph
        # if there is a cycle then don't add to final list
        # to check if there is a cycle in directed graph, use
        # 3-coloring DFS

        for node in range(len(graph)):
            if dfs(node, graph):
                ans.append(node)

        return ans
