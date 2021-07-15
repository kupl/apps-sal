class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        queue = [(0, True, 0), (0, False, 0)]
        result = [-1]*n
        result[0] = 0
        visited = set()
        
        while queue:
            node, red, dist = queue.pop(0)
            if (node, red) in visited:
                continue
            visited.add((node, red))
            if red:
                for edge in blue_edges:
                    if edge[0] == node:
                        if result[edge[1]] == -1:
                            result[edge[1]] = dist + 1
                        queue.append((edge[1], False, dist+1))
            
            else:
                for edge in red_edges:
                    if edge[0] == node:
                        if result[edge[1]] == -1:
                            result[edge[1]] = dist + 1
                        queue.append((edge[1], True, dist+1))
        
        return result
