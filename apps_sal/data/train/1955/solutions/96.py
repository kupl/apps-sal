class Solution:

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:

        def dfs(u, cc):
            cc.append(u)
            visited_set.add(u)
            if u in graph:
                for v in graph[u]:
                    if v not in visited_set:
                        dfs(v, cc)
        if len(pairs) == 0:
            return s
        graph = {}
        for (u, v) in pairs:
            if u in graph:
                graph[u].append(v)
            else:
                graph[u] = [v]
            if v in graph:
                graph[v].append(u)
            else:
                graph[v] = [u]
        result = [c for c in s]
        visited_set = set()
        for u in graph:
            if u not in visited_set:
                cc = []
                dfs(u, cc)
                cc.sort()
                auxr = [s[i] for i in cc]
                auxr.sort()
                for (i, index) in enumerate(cc):
                    result[index] = auxr[i]
        return ''.join(result)
