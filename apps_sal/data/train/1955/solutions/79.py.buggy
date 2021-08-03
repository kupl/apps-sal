class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        def union(x, y):
            graph[find(x)] = find(y)
        
        def find(x):
            path = []
            if x not in graph:
                return x
            while graph[x] != x:
                path.append(x)
                x = graph[x]
            for n in path:
                graph[n] = x
            return x

        graph = {}
        
        for u, v in pairs:
            if u not in graph:
                graph[u] = u
            if v not in graph:
                graph[v] = v
            union(u, v)
            
        ans = []
        comp = collections.defaultdict(list)
        for i, c in enumerate(s):
            comp[find(i)].append(c)
        for v in comp.values():
            v.sort(reverse=True)
        for i in range(len(s)):
            ans.append(comp[find(i)].pop())
        return \"\".join(ans)
