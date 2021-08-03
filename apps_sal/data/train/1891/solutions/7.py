class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def dfs(cols, diag_45, diag_135, depth=0):
            #print(' ' * depth, 'cols =', cols, 'diag_45 =', diag_45, 'diag_135 =', diag_135)
            row = len(cols)
            if row == n:
                result.append(cols)
                #print(' '*depth, 'Found placement!')
                return
            for col in range(n):
                if col not in cols and (row - col) not in diag_45 and (row + col) not in diag_135:
                    dfs(cols + [col], diag_45 + [row - col], diag_135 + [row + col], depth + 1)
            else:
                pass
                #print(' ' * depth, 'Placement not found; backtrack...')

        result = []
        dfs([], [], [])
        return [['.' * i + 'Q' + '.' * (n - i - 1) for i in sol] for sol in result]
