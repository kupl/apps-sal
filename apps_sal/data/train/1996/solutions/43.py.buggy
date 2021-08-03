\"\"\"
0 - unvisited
1 - currently visiting in the current DFS traversal
2 - already visited
\"\"\"
WHITE = 0
GRAY = 1
BLACK = 2

from collections import defaultdict
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        if not g:
            return []
        
        res = []
        g = defaultdict(list)
        n = len(graph)
        currRecurStack = [WHITE] * n
        visited = set()
        cycleExists = False
        
        for i in range(n):
            for vertex in graph[i]:
                g[i].append(vertex)
        
        
        for i in range(n):
            if i not in visited:
                cycleExists = dfsDetectCycle(g, visited, currRecurStack, i)
                if not cycleExists:
                    res.append(i)
        
        return res
                
            
    

def dfsDetectCycle(g, visited, currRecurStack, i):
    visited.add(i)
    currRecurStack[i] = GRAY
    
    neighbors = g[i]
    for nh in neighbors:
        if (nh not in visited and dfs(g, visited, currRecurStack, nh)): return True
        if (currRecurStack[nh] == GRAY): return True
    
    currRecurStack[i] = BLACK
    return False
















































from collections import defaultdict
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # visited = set()
        n = len(graph)
        # recur = [False] * n
        color = [0] * n
        g = defaultdict(list)
        ans = []
        
        for i in range(n):
            for nh in graph[i]:
                g[i].append(nh)
        
        for i in range(n):
            if not dfsCycle(g, i, color):
                ans.append(i)
        
        return ans

# alternate version with same logic
\"\"\"    
def dfsCycle2(g, node, recur, visited):
    visited.add(node)
    recur[node] = True
    
    for nh in g[node]:
        if (nh not in visited and dfsCycle2(g, nh, recur, visited)): return True
        if (recur[nh]): return True
    
    recur[node] = False
    return False
\"\"\"

def dfsCycle(g, node, color):
    color[node] = 1
    neighbours = g[node]
    
    for nh in neighbours:
        if (color[nh] == 0 and dfsCycle(g, nh, color)): return True
        if (color[nh] == 1): return True
    
    color[node] = 2
    return False
