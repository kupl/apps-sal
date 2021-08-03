class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        
        edgeList = {i:[] for i in range(n)}
        
        for u, v in red_edges:
            edgeList[u].append([v, \"red\"])
        
        for u, v in blue_edges:
            edgeList[u].append([v, \"blue\"])
        
        visited = set()
        
        queue = [[0, 0, \"\"]]
        ans = [float('inf')]*n
        ans[0] = 0
        
        while queue:
            node, node_cost, prev_color = queue.pop(0)
            for dest, color in edgeList[node]:
                
                if (prev_color == \"\" or color != prev_color) and (dest, color) not in visited:
                    visited.add((dest, color))
                    queue.append([dest, node_cost+1, color])
                    ans[dest] = min(ans[dest], node_cost+1)
            
        for i in range(len(ans)):
            if ans[i] == float('inf'):
                ans[i] = -1
        return ans
            
            
