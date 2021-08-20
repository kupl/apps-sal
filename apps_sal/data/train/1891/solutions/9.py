class Solution:

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        def dfs(n, a, b, c, ans, d):
            if n == 0:
                ans = ans.append([i * '.' + 'Q' + (len(a) - i - 1) * '.' for i in d])
                return None
            for i in range(len(a)):
                if a[i] or b[n - 1 + i] or c[len(a) - 1 - i + n - 1]:
                    continue
                (a[i], b[n - 1 + i], c[len(a) - 1 - i + n - 1]) = (True, True, True)
                d[n - 1] = i
                dfs(n - 1, a, b, c, ans, d)
                (a[i], b[n - 1 + i], c[len(a) - 1 - i + n - 1]) = (False, False, False)
            return None
        a = [False for i in range(n)]
        b = [False for i in range(n * 2 - 1)]
        c = [False for i in range(n * 2 - 1)]
        d = [0 for i in range(n)]
        ans = []
        dfs(n, a, b, c, ans, d)
        return ans
