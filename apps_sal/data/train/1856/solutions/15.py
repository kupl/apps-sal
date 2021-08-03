class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        num_steps_horizontal = [[float('inf') for _ in range(n)] for _ in range(n)]
        num_steps_vertical = [[float('inf') for _ in range(n)] for _ in range(n)]

        if not (grid[0][0] == grid[0][1] == 0):
            raise ValueError

        # initialization
        num_steps_horizontal[0][0] = 0
        for col in range(1, n - 1):
            if grid[0][col + 1] == 0:
                num_steps_horizontal[0][col] = 1 + num_steps_horizontal[0][col - 1]
            else:
                break

        # iterate over num_steps_horizontal and num_steps_vertical
        for row in range(n):
            for col in range(n):
                if col < n - 1 and grid[row][col] == grid[row][col + 1] == 0:
                    num_steps_horizontal[row][col] = min(
                        num_steps_horizontal[row][col],
                        1 + num_steps_horizontal[row][col - 1],  # from left
                        1 + num_steps_horizontal[row - 1][col],  # from above
                    )
                if row < n - 1 and grid[row][col] == grid[row + 1][col] == 0:
                    num_steps_vertical[row][col] = min(
                        num_steps_vertical[row][col],
                        1 + num_steps_vertical[row][col - 1],  # from left
                        1 + num_steps_vertical[row - 1][col],  # from above
                    )
                if (col < n - 1 and row < n - 1
                   and grid[row][col] == grid[row][col + 1] == 0
                   and grid[row + 1][col] == grid[row + 1][col + 1] == 0):
                    num_steps_horizontal[row][col] = min(num_steps_horizontal[row][col], 1 + num_steps_vertical[row][col])
                    num_steps_vertical[row][col] = min(num_steps_vertical[row][col], 1 + num_steps_horizontal[row][col])

        if num_steps_horizontal[-1][-2] < float('inf'):
            return num_steps_horizontal[-1][-2]
        else:
            return -1
