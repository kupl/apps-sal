class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        def dfs(i):
            visited[i] = True
            component.append(i)
            for adj in adj_list[i]:
                if not visited[adj]:
                    dfs(adj)
        
        adj_list = collections.defaultdict(list)
        visited = [False] * len(s)
        for pair in pairs:
            adj_list[pair[0]].append(pair[1])
            adj_list[pair[1]].append(pair[0])
            
        ans = list(s)
    
        for index in range(len(s)):
            if not visited[index]:
                component = []
                dfs(index)
                component.sort()
                lst_chars = [ans[i] for i in component]
                lst_chars.sort()
                for i in range(len(lst_chars)): ans[component[i]] = lst_chars[i]
        
        return \"\".join(ans)
                
        
        
            
