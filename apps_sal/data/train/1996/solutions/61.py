class Solution:

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        dic = collections.defaultdict(list)
        for (i, e) in enumerate(graph):
            for j in e:
                dic[i].append(j)
        memo = {}

        def dfs(node):
            if not dic[node]:
                return True
            if node in memo:
                return memo[node]
            memo[node] = False
            if all((dfs(nxt) for nxt in dic[node])):
                memo[node] = True
            return memo[node]
        res = []
        for i in range(len(graph)):
            if dfs(i):
                res.append(i)
        return res
