class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(i, j):
            dic[(i, j)] = curr
            count[curr] += 1
            for dx, dy in directions:
                a, b = i + dx, j + dy
                if 0 <= a < m and 0 <= b < n and grid[a][b] == 1 and (a, b) not in dic:
                    dfs(a, b)

        def neighbours(i, j, adj):
            for dx, dy in directions:
                a, b = i + dx, j + dy
                if 0 <= a < m and 0 <= b < n and grid[a][b] == 1 and dic[(a, b)] not in adj:
                    adj.add(dic[(a, b)])

            return adj

        curr, dic, count, res = 0, {}, collections.defaultdict(int), 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in dic:
                    curr += 1
                    dfs(i, j)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res, count[dic[(i, j)]])
                else:
                    res = max(res, sum(count[r] for r in neighbours(i, j, set())) + 1)

        return res
