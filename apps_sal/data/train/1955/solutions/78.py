class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        res = list(s)
        adj = defaultdict(set)
        for a, b in pairs:
            adj[a].add(b)
            adj[b].add(a)

        while adj:
            i = next(iter(adj))
            v = []
            self.dfs(i, adj, v)
            v = sorted(v)
            chars = sorted([s[i] for i in v])
            for i, c in enumerate(chars):
                res[v[i]] = c

        return ''.join(res)

    def dfs(self, i, adj, res):
        if i in adj:
            res.append(i)
            for j in adj.pop(i):
                self.dfs(j, adj, res)
