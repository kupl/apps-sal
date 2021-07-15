from itertools import count
from collections import Counter

class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        # color the components
        colors = dict()
        c = count()
        
        def dfs(node, color):
            colors[node] = color
            
            for nei, adj in enumerate(graph[node]):
                if adj and nei not in colors:
                    dfs(nei, color)
                    
        for node in range(len(graph)):
            if node not in colors:
                dfs(node, next(c))
        
        
        # count sizes of each component
        size = Counter(list(colors.values()))
        
        
        # find components with only one malware inside
        malware_count = Counter()
        for node in initial:
            malware_count[colors[node]] += 1
            
        #print(malware_count)
        #print(size)
        
        # find the component with the most nodes and only 1 malware
        ans = None
        ans_nodes = 0
        for x in initial:
            c = colors[x]
            if malware_count[c] != 1:
                continue
            if size[c] > ans_nodes:
                ans = x
                ans_nodes = size[c]
            elif size[c] == ans_nodes:
                ans = min(ans, x)
                
        return ans if ans else min(initial)

