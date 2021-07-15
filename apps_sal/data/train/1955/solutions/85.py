class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        S=s
        N = len(S)
        graph = [[] for _ in range(N)]
        for u, v in pairs:
            graph[u].append(v)
            graph[v].append(u)
        ans = [None] * N
        
        seen = [False] * N
        for u in range(N):
            if not seen[u]:
                seen[u] = True
                stack = [u]
                component = []
                while stack:
                    node = stack.pop()
                    component.append(node)
                    for nei in graph[node]:
                        if not seen[nei]:
                            seen[nei] = True
                            stack.append(nei)
                
                component.sort()
                letters = sorted(S[i] for i in component)
                for ix, i in enumerate(component):
                    letter = letters[ix]
                    ans[i] = letter
        return \"\".join(ans)
        
