class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def is_floor(i, j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] != '#'

        def bfs(start_i, start_j, box_i, box_j):
            visited, queue, reach_list = [[0 for _ in range(n)] for _ in range(m)], [(start_i, start_j)], []
            visited[start_i][start_j] = 1
            reach_list_upbound = len([1 for delta_i, delta_j in [(0, -1), (-1, 0), (0, 1), (1, 0)] if is_floor(box_i + delta_i, box_j + delta_j)])
            while queue:
                start_i, start_j = queue.pop(0)
                for delta_i, delta_j in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                    if start_i + delta_i == box_i and start_j + delta_j == box_j:
                        reach_list.append((delta_i, delta_j))
                        if len(reach_list) >= reach_list_upbound:
                            return reach_list
                    elif is_floor(start_i + delta_i, start_j + delta_j) and visited[start_i + delta_i][start_j + delta_j] == 0:
                        visited[start_i + delta_i][start_j + delta_j] = 1
                        queue.append((start_i + delta_i, start_j + delta_j))
            return reach_list
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'S':
                    source = (i, j)
                elif grid[i][j] == 'B':
                    box = (i, j)
                elif grid[i][j] == 'T':
                    target = (i, j)
        queue = [(source, box, 0)]
        visited = set()
        while queue:
            source, box, depth = queue.pop(0)
            if box[0] == target[0] and box[1] == target[1]:
                return depth
            reach_list = bfs(source[0], source[1], box[0], box[1])
            for mov in reach_list:
                s, b = (box[0], box[1]), (box[0] + mov[0], box[1] + mov[1])
                if is_floor(b[0], b[1]) and (s, b) not in visited:
                    visited.add((s, b))
                    queue.append((s, b, depth + 1))
        return -1
