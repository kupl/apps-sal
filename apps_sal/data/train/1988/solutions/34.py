class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        # 4:43 10/2/20
        graph = [collections.defaultdict(set), collections.defaultdict(set)]

        for i, j in red_edges:
            graph[0][i].add(j)

        for i, j in blue_edges:
            graph[1][i].add(j)

        ans = [math.inf] * n
        
        stack = [(0, 0, 0), (1, 0, 0)]
        
        for color, node, dist in stack:
            ans[node] = min(ans[node], dist)
            neighbors = list(graph[color][node])
            for nei in neighbors:
                graph[color][node].remove(nei)
                stack.append((1-color, nei, dist+1))
        
        return [-1 if x == math.inf else x for x in ans]
        

