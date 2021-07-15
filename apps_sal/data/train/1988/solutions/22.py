class Solution:
    def shortestAlternatingPaths(
        self, 
        n: int, 
        red_edges: List[List[int]], 
        blue_edges: List[List[int]],
    ) -> List[int]:
        red_adj = [[] for i in range(n)]
        blue_adj = [[] for i in range(n)]
        for edge in red_edges:
            red_adj[edge[0]].append(edge[1])
        for edge in blue_edges:
            blue_adj[edge[0]].append(edge[1])
        result = []
        for i in range(n):
            start_red = self.shortestPath(red_adj, blue_adj, True, i)
            start_blue = self.shortestPath(red_adj, blue_adj, False, i)
            if start_red == -1:
                result.append(start_blue)
            elif start_blue == -1:
                result.append(start_red)
            elif start_red < start_blue:
                result.append(start_red)
            else:
                result.append(start_blue)
        return result
        
    def shortestPath(
        self,
        red_adj: List[List[int]], 
        blue_adj: List[List[int]],
        startRed: bool,
        X: int,
    ) -> int:
        red_visited = set()
        blue_visited = set()
        bfs = [(0, startRed, 0)]
        while len(bfs) > 0:
            node, is_red, depth = bfs.pop(0)
            if node == X:
                return depth
            if is_red and node in red_visited:
                continue
            elif not is_red and node in blue_visited:
                continue
            if is_red:
                red_visited.add(node)
                for n in blue_adj[node]:
                    if n not in blue_visited:
                        bfs.append((n, False, depth + 1))
            else:
                blue_visited.add(node)
                for n in red_adj[node]:
                    if n not in red_visited:
                        bfs.append((n, True, depth + 1))
        return -1
