class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        def dfs(node, parent):
            for child in graph[node]:
                if child != parent:
                    dfs(child, node)
                    count_self_and_children[node] += count_self_and_children[child]
                    res[node] += res[child] + count_self_and_children[child]

        def dfs2(node, parent):
            for child in graph[node]:
                if child != parent:
                    res[child] = res[node] + N - 2 * count_self_and_children[child]
                    dfs2(child, node)

        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        count_self_and_children = [1] * N
        res = [0] * N
        dfs(0, None)
        dfs2(0, None)

        return res
