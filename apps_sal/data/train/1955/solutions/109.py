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
        for u, v in pairs:
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
        for i in range(len(s)):
            if visited_set[i] == 0:
                cc += 1
                dfs(i, cc)

        dd = {}
        for i, key in enumerate(visited_set):
            if key in dd:
                heapq.heappush(dd[key], s[i])
            else:
                dd[key] = [s[i]]

        return ''.join(heapq.heappop(dd[key]) for key in visited_set)
