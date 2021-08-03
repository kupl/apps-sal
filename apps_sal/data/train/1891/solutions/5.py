class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def dfs(queens, xy_dif, xy_sum):
            p = len(queens)
            if p == n:
                res.append(queens)
                return
            for i in range(n):
                if i not in queens and p - i not in xy_dif and p + i not in xy_sum:
                    dfs(queens + [i], xy_dif + [p - i], xy_sum + [p + i])
        res = []
        dfs([], [], [])
        return [["." * i + "Q" + '.' * (n - i - 1) for i in sol] for sol in res]
