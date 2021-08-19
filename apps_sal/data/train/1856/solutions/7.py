from collections import deque


class Solution:

    def minimumMoves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = {(0, 1, 0, 0)}
        moves = -1
        queue = deque([(0, 1, 0, 0)])
        while queue:
            level_len = len(queue)
            moves += 1
            for _ in range(level_len):
                tp = queue.popleft()
                (curr, last) = (tp[:2], tp[2:])
                if tp == (n - 1, n - 1, n - 1, n - 2):
                    return moves
                if curr[1] + 1 < n and last[1] + 1 < n and (grid[curr[0]][curr[1] + 1] == 0) and (grid[last[0]][last[1] + 1] == 0) and ((curr[0], curr[1] + 1, last[0], last[1] + 1) not in visited):
                    visited.add((curr[0], curr[1] + 1, last[0], last[1] + 1))
                    queue.append((curr[0], curr[1] + 1, last[0], last[1] + 1))
                if curr[0] + 1 < n and last[0] + 1 < n and (grid[curr[0] + 1][curr[1]] == 0) and (grid[last[0] + 1][last[1]] == 0) and ((curr[0] + 1, curr[1], last[0] + 1, last[1]) not in visited):
                    visited.add((curr[0] + 1, curr[1], last[0] + 1, last[1]))
                    queue.append((curr[0] + 1, curr[1], last[0] + 1, last[1]))
                if curr[0] == last[0] and curr[0] + 1 < n and (grid[curr[0] + 1][curr[1]] == 0) and (grid[last[0] + 1][last[1]] == 0) and ((curr[0] + 1, curr[1] - 1, last[0], last[1]) not in visited):
                    visited.add((curr[0] + 1, curr[1] - 1, last[0], last[1]))
                    queue.append((curr[0] + 1, curr[1] - 1, last[0], last[1]))
                if curr[1] == last[1] and curr[1] + 1 < n and (grid[curr[0]][curr[1] + 1] == 0) and (grid[last[0]][last[1] + 1] == 0) and ((curr[0] - 1, curr[1] + 1, last[0], last[1]) not in visited):
                    visited.add((curr[0] - 1, curr[1] + 1, last[0], last[1]))
                    queue.append((curr[0] - 1, curr[1] + 1, last[0], last[1]))
        return -1
