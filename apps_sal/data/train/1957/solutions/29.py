class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        from collections import deque, defaultdict
        moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        rows = len(grid)
        cols = len(grid[0])

        seen = set()
        queue = deque()
        queue.append((0, 0, k, 0))

        while len(queue) > 0:
            row, col, eliminations_left, path_length = queue.popleft()

            if row == rows - 1 and col == cols - 1:
                return path_length

            for move in moves:
                next_row, next_col = row + move[0], col + move[1]

                if not (0 <= next_row < rows) or not (0 <= next_col < cols):
                    continue

                if (next_row, next_col, eliminations_left) in seen:
                    continue

                if grid[next_row][next_col] == 1:
                    if eliminations_left > 0:
                        seen.add((next_row, next_col, eliminations_left))
                        queue.append((next_row, next_col, eliminations_left - 1, path_length + 1))
                else:
                    seen.add((next_row, next_col, eliminations_left))
                    queue.append((next_row, next_col, eliminations_left, path_length + 1))

        return -1
