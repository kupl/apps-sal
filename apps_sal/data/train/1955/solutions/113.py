class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        def dfs(u, cc):
            cc.append(u)
            visited_set.add(u)
            if u in graph:
                for v in graph[u]:
                    if v not in visited_set:
                        dfs(v, cc)

        M = len(pairs)
        if M == 0:
            return s

        graph = defaultdict(list)
        for u,v in pairs:
            graph[u].append(v)
            graph[v].append(u)

        result = [c for c in s]
        visited_set = set()
        for u in graph:
            if u not in visited_set:
                cc = []
                dfs(u, cc)
                cc.sort()
                auxr = [s[i] for i in cc]
                auxr.sort()
                for i, index in enumerate(cc):
                    result[index] = auxr[i]
        return ''.join(result)
