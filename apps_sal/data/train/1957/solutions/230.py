class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        H, W = len(grid), len(grid[0])
        if k >= H + W - 3:
            return H + W - 2

        step = 0
        node_list = [(0, 0, k)]
        visited = set()
        while node_list:
            new_list = []
            for node in node_list:
                if node in visited:
                    continue
                visited.add(node)
                x, y, k_remains = node
                if x == H - 1 and y == W - 1:
                    return step
                for i, j in [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]:
                    if i < 0 or i >= H or j < 0 or j >= W:
                        continue
                    if grid[i][j] == 0:
                        new_list.append((i, j, k_remains))
                    elif grid[i][j] == 1 and k_remains > 0:
                        new_list.append((i, j, k_remains - 1))

            step += 1
            node_list = new_list

        return -1
