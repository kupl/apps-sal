class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                temp = board[i][j]
                board[i][j] = 'D'
                if self.isValid(board, i, j, temp) == False:
                    return False
                board[i][j] = temp
        return True

    def isValid(self, board, x, y, temp):
        for i in range(9):
            if board[i][y] == temp:
                return False
        for i in range(9):
            if board[x][i] == temp:
                return False
        for i in range(3):
            for j in range(3):
                if board[x // 3 * 3 + i][y // 3 * 3 + j] == temp:
                    return False
        return True
