class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        def dfs(i):
            visited[i] = True
            component.append(i)
            for j in adj_list[i]:
                if not visited[j]:
                    dfs(j)
        n = len(s)
        adj_list = [[] for _ in range(n)]
        for i, j in pairs:
            adj_list[i].append(j)
            adj_list[j].append(i)
        visited = [False for _ in range(n)]
        s = list(s)
        for i in range(n):
            if not visited[i]:
                component = []
                dfs(i)
                component.sort()
                chars = [s[k] for k in component]
                chars.sort()
                for i in range(len(component)):
                    s[component[i]] = chars[i]
        return ''.join(s)
