class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        edges = defaultdict(list)
        
        for p in pairs:
            edges[p[0]].append(p[1])
            edges[p[1]].append(p[0])
        visited = [False for i in range(n)]
        
        def dfs(node):
            visited[node] = True
            component.append(node)
            for neighbor in edges[node]:
                if not visited[neighbor]:
                    dfs(neighbor)
                    
        connected_components = []
        for i in range(n):
            if not visited[i]:
                component = []
                dfs(i)
                connected_components.append(component)
        #print(connected_components)
        ans = [\" \" for i in range(n)]
        for component in connected_components:
            indexes = sorted(component)
            chars = [s[i] for i in indexes]
            chars = sorted(chars)
            for i in range(len(indexes)):
                ans[indexes[i]] = chars[i]
        #print(ans)
        return ''.join(ans)
