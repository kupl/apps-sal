from collections import defaultdict
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        def dfs(x):
            visited.add(x)
            component.append(x)
            for ele in adjacencyList[x]:
                if ele not in visited:
                    dfs(ele)
            
        adjacencyList = [[] for x in range(len(s))]
        for pair in pairs:
            # print(pair, adjacencyList, len(s))
            adjacencyList[pair[0]].append(pair[1])
            adjacencyList[pair[1]].append(pair[0])
        
        
        visited = set()
        ans = list(s)
        for x in range(len(s)):
            if x not in visited:
                component = []
                dfs(x)
                lst = []
                component.sort()
                for y in component:
                    lst.append(s[y])
                lst.sort()
                i = 0
                for y in component:
                    ans[y] = lst[i]
                    i+=1
        return \"\".join(ans)
                    
                
        
    
