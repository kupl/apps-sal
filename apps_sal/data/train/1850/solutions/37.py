class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:

        graph = [set() for _ in range(N)]
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])

        count = [1] * N
        ans = [0] * N

        def dfs(node, parent):
            for child in graph[node]:
                if child != parent:
                    dfs(child, node)
                    count[node] += count[child]
                    ans[node] += ans[child] + count[child]

        def dfs2(node, parent):
            for child in graph[node]:
                if child != parent:

                    ans[child] = ans[node] - count[child] + N - count[child]
                    dfs2(child, node)

        dfs(0, None)

        dfs2(0, None)

        return ans
