class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        s = list(s)
        graph = [[] for _ in range(len(s))]
        for u,v in pairs:
            graph[u].append(v)
            graph[v].append(u)
        stack = []
        vis = [False]*len(s)
        self.res = \"\"
        self.index = []
        def dfs(graph,u):
            vis[u] = True
            self.res += s[u]
            self.index.append(u)
            for v in graph[u]:
                if not vis[v]:
                    dfs(graph,v)
        for i in range(len(graph)):
            if not vis[i]:
                self.res = \"\"
                self.index = []
                dfs(graph,i)
                self.index.sort()
                self.res = sorted(list(self.res))
                for i in range(len(self.index)):
                    s[self.index[i]] = self.res[i]
        return ''.join(s)

