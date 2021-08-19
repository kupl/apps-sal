class Solution:

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        start = end = None
        remain = 0
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n] == 1:
                    start = (m, n)
                elif grid[m][n] == 2:
                    end = (m, n)
                if grid[m][n] == 0:
                    remain += 1
        if start is None or end is None:
            return 0
        return self._helper(grid, start[0], start[1], end[0], end[1], remain + 1)

    def _helper(self, grid: List[List[int]], start_m: int, start_n: int, end_m: int, end_n: int, remain: int) -> int:
        if 0 <= start_m < len(grid) and 0 <= start_n < len(grid[0]) and (grid[start_m][start_n] > -1):
            if remain < 0:
                return 0
            elif remain == 0 and start_m == end_m and (start_n == end_n):
                return 1
            count = 0
            grid[start_m][start_n] = -2
            count += self._helper(grid, start_m + 1, start_n, end_m, end_n, remain - 1)
            count += self._helper(grid, start_m, start_n + 1, end_m, end_n, remain - 1)
            count += self._helper(grid, start_m - 1, start_n, end_m, end_n, remain - 1)
            count += self._helper(grid, start_m, start_n - 1, end_m, end_n, remain - 1)
            grid[start_m][start_n] = 0
            return count
        return 0
