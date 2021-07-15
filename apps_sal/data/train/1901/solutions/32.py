class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])

        max_size = 0

        # mark islands
        area_sizes = [0, 0]  # starts from  2

        def mark(i, j) -> int:  # size
            if not (0 <= i < M and 0 <= j < N):
                return 0
            if grid[i][j] != 1:
                return 0
            else:
                grid[i][j] = len(area_sizes)
            return 1 + mark(i - 1, j) + mark(i + 1, j) + mark(i, j - 1) + mark(i, j + 1)

        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    area_sizes.append(mark(i, j))

        max_size = max(max_size, *area_sizes)  # FIXME: bug: 忘記考慮沒有 0 的狀況

        # for each 0, try to find max size
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 0:
                    ids = set() # FIXME: bug: 忘記 dedup, 造成重複算
                    if 0 <= i - 1:
                        ids.add(grid[i - 1][j])
                    if i + 1 < M:
                        ids.add(grid[i + 1][j])
                    if 0 <= j - 1:
                        ids.add(grid[i][j - 1])
                    if j + 1 < N:
                        ids.add(grid[i][j + 1])

                    max_size = max(max_size, sum(area_sizes[id] for id in ids) + 1)

        return max_size

