class Solution:

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:

        def dfs(root, res):
            if letters[root] == 1:
                return
            letters[root] = 1
            res.append(root)
            for node in graph[root]:
                dfs(node, res)
        letters = [0] * len(s)
        graph = [[] for _ in range(len(s))]
        for (a, b) in pairs:
            graph[a].append(b)
            graph[b].append(a)
        res = list(s)
        for i in range(len(s)):
            if letters[i] == 0:
                visited = []
                dfs(i, visited)
                nodes = []
                for node in visited:
                    nodes.append(res[node])
                nodes.sort()
                visited.sort()
                for (node, index) in zip(nodes, visited):
                    res[index] = node
        return ''.join(res)
