class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        steps = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def checkValid(x, y):
            return 0 <= x < m and 0 <= y < n
        d = {}
        @lru_cache(None)
        def dp(i, j, p):
            nonlocal steps
            if p < 0:
                return float('inf')
            if i == m - 1 and j == n - 1:
                return 0
            d[(i, j, p)] = min(d.get((i, j, p), float('inf')), steps)
            res = float('inf')
            if steps >= m * n:
                # print(steps)
                return steps
            for dr in directions:
                x, y = i + dr[0], j + dr[1]
                if x < 0 or x >= m or y < 0 or y >= n:
                    continue
                if grid[x][y] == 0:
                    if steps + 1 <= d.get((x, y, p), float('inf')):
                        steps += 1
                        res = min(res, dp(x, y, p))
                        steps -= 1
                else:
                    if steps + 1 <= d.get((x, y, p - 1), float('inf')):
                        steps += 1
                        grid[x][y] = 0
                        res = min(res, dp(x, y, p - 1))
                        grid[x][y] = 1
                        steps -= 1
            return res + 1
        ans = float('inf')
        # print(\"k = \", k)
        ans = min(ans, dp(0, 0, k))
        # for i in range(k, -1, -1):
        #     ans = min(ans, dp(m - 1, n - 1, i))
            # print(dp(m - 1, n - 1, i))
        # print(dp(m - 1, n - 1, 283))
        if ans > 10**10:
            return -1
        return ans
            
                    
                
            

