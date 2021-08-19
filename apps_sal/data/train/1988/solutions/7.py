class Solution:

    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        shortest = [-1] * n
        shortest[0] = 0
        self.BFS(shortest, red_edges, blue_edges, True)
        self.BFS(shortest, red_edges, blue_edges, False)
        return shortest

    def BFS(self, shortest, red_edges, blue_edges, red):
        path_len = 1
        seen_r = {0}
        seen_b = {0}
        current = [0]
        while current:
            if red:
                edges = red_edges
                seen = seen_r
                red = False
            else:
                edges = blue_edges
                seen = seen_b
                red = True
            new_layer = []
            for node in current:
                for edge in edges:
                    if edge[0] == node:
                        if edge[1] not in seen:
                            new_node = edge[1]
                            seen.add(new_node)
                            new_layer.append(new_node)
                            if shortest[new_node] == -1:
                                shortest[new_node] = path_len
                            else:
                                shortest[new_node] = min(shortest[new_node], path_len)
            current = new_layer
            path_len += 1
