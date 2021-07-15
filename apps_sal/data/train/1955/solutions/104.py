class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        def dfs(u, cc):
            visited_set[u] = cc
            if u in graph:
                for v in graph[u]:
                    if visited_set[v] == 0:
                        dfs(v, cc)

        if len(pairs) == 0:
            return s

        graph = {}
        for u,v in pairs:
            if u in graph:
                graph[u].append(v)
            else:
                graph[u] = [v]
            if v in graph:
                graph[v].append(u)
            else:
                graph[v] = [u]

        visited_set = [0 for i in range(len(s))]
        cc = 0
        for u in graph:
            if visited_set[u] == 0:
                cc += 1
                dfs(u, cc)

        dd = {}
        result = [c for c in s]
        for i,key in enumerate(visited_set):
            if key != 0:
                if key in dd:
                    dd[key].append(s[i]);
                else:
                    dd[key] = [s[i]]
        for key in dd:
            dd[key].sort(reverse=True)
        for i, key in enumerate(visited_set):
            if key != 0:
                result[i] = dd[key].pop()

        return ''.join(result)
