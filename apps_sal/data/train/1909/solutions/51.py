class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        left_top = []
        for r in range(len(grid)):
            left_top.append([0] * len(grid[0]))
        right_bottom = []
        for r in range(len(grid)):
            right_bottom.append([0] * len(grid[0]))
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                ans = 0
                while r - ans >= 0 and c - ans >= 0 and grid[r - ans][c] == 1 and grid[r][c - ans] == 1:
                    ans += 1
                left_top[r][c] = ans
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                ans = 0
                while r + ans < len(grid) and c + ans < len(grid[0]) and grid[r + ans][c] == 1 and grid[r][c + ans] == 1:
                    ans += 1
                right_bottom[r][c] = ans

        max_len = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                ans = 0
                for i in range(left_top[r][c]):
                    if right_bottom[r - i][c - i] > i:
                        ans = i + 1
                max_len = max(max_len, ans)
        return max_len**2
