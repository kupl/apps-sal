class Solution:

    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        (O, X) = (0, 0)
        for r in board:
            for c in r:
                if c == 'O':
                    O += 1
                elif c == 'X':
                    X += 1
        if O - X > 0:
            return False
        if X - O > 1:
            return False
        for c in range(2):
            if board[0][c] == 'X' and board[1][c] == 'X' and (board[2][c] == 'X'):
                return X - O == 1
            if board[c][0] == 'X' and board[c][1] == 'X' and (board[c][2] == 'X'):
                return X - O == 1
        if board[0][0] == 'X' and board[1][1] == 'X' and (board[2][2] == 'X'):
            return X - O == 1
        if board[2][0] == 'X' and board[1][1] == 'X' and (board[0][2] == 'X'):
            return X - O == 1
        for c in range(2):
            if board[0][c] == 'O' and board[1][c] == 'O' and (board[2][c] == 'O'):
                return X - O == 0
            if board[c][0] == 'O' and board[c][1] == 'O' and (board[c][2] == 'O'):
                return X - O == 0
        if board[0][0] == 'O' and board[1][1] == 'O' and (board[2][2] == 'O'):
            return X - O == 0
        if board[2][0] == 'O' and board[1][1] == 'O' and (board[0][2] == 'O'):
            return X - O == 0
        return True
