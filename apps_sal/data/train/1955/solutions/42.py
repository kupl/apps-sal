class Solution:

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        graph = defaultdict(list)
        visited = [False] * len(s)
        out = [None] * len(s)
        for (u, v) in pairs:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(i, stash):
            visited[i] = True
            stash.append(i)
            for vertice in graph[i]:
                if not visited[vertice]:
                    stash = dfs(vertice, stash)
            return stash
        for i in range(len(s)):
            if not visited[i]:
                indices = sorted(dfs(i, []))
                letters = sorted([s[i] for i in indices])
                for j in range(len(indices)):
                    out[indices[j]] = letters[j]
        return ''.join(out)
