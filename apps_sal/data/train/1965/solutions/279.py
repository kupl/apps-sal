class Solution:

    def dfs(self, i, a, b, types):
        b[i] = 1
        for k in a[i]:
            if k[0] in types and b[k[1]] == 0:
                self.dfs(k[1], a, b, types)

    def check(self, a, types) -> int:
        n = len(a)
        b = [0] * n
        ans = 0
        for i in range(n):
            if b[i] == 0:
                self.dfs(i, a, b, types)
                ans += 1
        return ans

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        a = []
        for i in range(n):
            a.append([])
        p = 0
        for edge in edges:
            u = edge[1] - 1
            v = edge[2] - 1
            a[u].append([edge[0], v])
            a[v].append([edge[0], u])
            if edge[0] == 3:
                p += 1
        if self.check(a, [1, 3]) > 1 or self.check(a, [2, 3]) > 1:
            return -1
        edge3 = n - self.check(a, [3])
        return len(edges) - (n - 1) * 2 + edge3
