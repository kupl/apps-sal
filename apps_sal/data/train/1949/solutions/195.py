class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        ans = 0

        def bfs(a, s, d, f):
            nonlocal ans
            q = collections.deque([(a, s, d, f)])

            while q:
                j, k, tot, seen = q.popleft()
                for m, n in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    jm, kn = j + m, k + n
                    if jm > -1 and kn > -1 and jm < len(grid) and kn < len(grid[0]) and grid[jm][kn] and (jm, kn) not in seen:
                        q.append((jm, kn, tot + grid[jm][kn], seen | {(jm, kn)}))
                    else:
                        ans = max(ans, tot)

        for i in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[i][x]:
                    bfs(i, x, grid[i][x], {(i, x)})

        return ans
