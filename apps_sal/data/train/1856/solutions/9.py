class Solution:

    def minimumMoves(self, grid: List[List[int]]) -> int:
        visited = set()
        queue = deque()
        n = len(grid)
        queue.append((0, 0, 0, 1))
        visited.add(queue[0])
        res = 0
        target = (n - 1, n - 2, n - 1, n - 1)
        while queue:
            size = len(queue)
            for _ in range(size):
                curr = queue.popleft()
                if curr == target:
                    return res
                horizontal = curr[0] == curr[2]
                moves = []
                if curr[3] < n - 1 and grid[curr[0]][curr[1] + 1] == 0 and (grid[curr[2]][curr[3] + 1] == 0):
                    moves.append((curr[0], curr[1] + 1, curr[2], curr[3] + 1))
                if curr[2] < n - 1 and grid[curr[0] + 1][curr[1]] == 0 and (grid[curr[2] + 1][curr[3]] == 0):
                    moves.append((curr[0] + 1, curr[1], curr[2] + 1, curr[3]))
                if horizontal and curr[2] < n - 1 and (grid[curr[0] + 1][curr[1]] == 0) and (grid[curr[2] + 1][curr[3]] == 0):
                    moves.append((curr[0], curr[1], curr[0] + 1, curr[1]))
                if not horizontal and curr[3] < n - 1 and (grid[curr[0]][curr[1] + 1] == 0) and (grid[curr[2]][curr[3] + 1] == 0):
                    moves.append((curr[0], curr[1], curr[0], curr[1] + 1))
                for move in moves:
                    if move not in visited:
                        visited.add(move)
                        queue.append(move)
            res += 1
        return -1
