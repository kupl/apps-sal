class Solution:

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        anslist = sum(([(i, c), (c, j), (i // 3, j // 3, c)] for (i, row) in enumerate(board) for (j, c) in enumerate(row) if c != '.'), [])
        return len(anslist) == len(set(anslist))
