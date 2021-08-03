class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        def expand_square(r, c):
            left, top = [r, c], [r, c]
            side = 0
            area = 0
            while left[0] < n and top[1] < m and grid[left[0]][left[1]] == 1 and grid[top[0]][top[1]] == 1:
                valid = True
                for row in range(top[0], left[0] + 1):
                    if grid[row][top[1]] == 0:
                        valid = False
                        break
                for col in range(left[1], top[1] + 1):
                    if grid[left[0]][col] == 0:
                        valid = False
                        break
                if valid:
                    area = (side + 1) ** 2
                top[1] += 1
                left[0] += 1
                side += 1

            return area

        max_area = 0
        for r in range(n):
            for c in range(m):
                max_area = max(max_area, expand_square(r, c))
        return max_area
