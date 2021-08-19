class Solution:

    def bfsHelper(self, adj_matrix, n):
        res = [1e10 for i in range(n)]
        queue = []
        queue.append([0, 0, 0])  # append [node,color traversed last,dist from 0]
        visited = set()  # each elem is (node, last traversed color)
        visited.add((0, 0))
        while queue:
            curr, color, dist = queue.pop(0)
            res[curr] = min(res[curr], dist)

            for neighbor in range(n):
                edge = adj_matrix[curr][neighbor]
                if edge == 0:  # if there is no edge
                    continue
                if color == 0:  # if we did not traverse to this node, can use any color
                    if edge in [1, 2]:
                        if (neighbor, edge) not in visited:
                            visited.add((neighbor, edge))
                            queue.append([neighbor, edge, dist + 1])
                    if edge == 3:
                        if (neighbor, 1) not in visited and color != 1:
                            visited.add((neighbor, 1))
                            queue.append([neighbor, 1, dist + 1])
                        if (neighbor, 2) not in visited and color != 2:
                            visited.add((neighbor, 2))
                            queue.append([neighbor, 2, dist + 1])
                elif color in [1, 2]:
                    if edge in [1, 2]:
                        if (color != edge):
                            if (neighbor, edge) not in visited:
                                visited.add((neighbor, edge))
                                queue.append([neighbor, edge, dist + 1])
                    if edge == 3:  # curr has red and blue edges
                        if (neighbor, 1) not in visited and color != 1:
                            visited.add((neighbor, 1))
                            queue.append([neighbor, 1, dist + 1])
                        if (neighbor, 2) not in visited and color != 2:
                            visited.add((neighbor, 2))
                            queue.append([neighbor, 2, dist + 1])

        for i in range(len(res)):
            if res[i] == 1e10:
                res[i] = -1

        return res

    def shortestAlternatingPaths(self, n, red_edges, blue_edges):
        # 0, no edge
        # 1, red edge
        # 2, blue edge
        # 3, both edges
        adj_matrix = [[0 for i in range(n)] for j in range(n)]
        for x, y in red_edges:
            adj_matrix[x][y] += 1
        for x, y in blue_edges:
            adj_matrix[x][y] += 2

        return self.bfsHelper(adj_matrix, n)
