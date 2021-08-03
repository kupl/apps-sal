class Solution:
    def getMaximumGold(self, a: List[List[int]]) -> int:

        def dfs(a, r, c, curSum, res):

            res[0] = max(res[0], curSum)

            temp = a[r][c]
            a[r][c] = -1

            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

            for d in directions:
                nr, nc = r + d[0], c + d[1]
                if nr >= 0 and nr < len(a) and nc >= 0 and nc < len(a[0]):
                    if a[nr][nc] > 0:
                        dfs(a, nr, nc, curSum + a[nr][nc], res)

            a[r][c] = temp

            return

        res = [0]
        for i in range(0, len(a)):
            for j in range(0, len(a[0])):
                if a[i][j] > 0:
                    dfs(a, i, j, a[i][j], res)

        return res[0]
