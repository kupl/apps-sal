class Solution:
    def isWin(self, board, c):
        for i in range(3):
            if board[0][i] == c and board[1][i] == c and board[2][i] == c:
                return True
        for i in range(3):
            if board[i][0] == c and board[i][1] == c and board[i][2] == c:
                return True
        if board[0][0] == c and board[1][1] == c and board[2][2] == c or \
                board[0][2] == c and board[1][1] == c and board[2][0] == c:
            return True

        return False

    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        o_cnt = 0
        x_cnt = 0
        for i in range(3):
            for j in range(3):
                x_cnt += 1 if board[i][j] == 'X' else 0
                o_cnt += 1 if board[i][j] == 'O' else 0

        if o_cnt > x_cnt or x_cnt > o_cnt + 1:
            return False
        if o_cnt == x_cnt and self.isWin(board, 'X') or x_cnt == o_cnt + 1 and self.isWin(board, 'O'):
            return False

        return True
