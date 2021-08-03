class Solution:
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        def Xwin(board):
            for r in range(2):
                if board[r] == 'XXX':
                    return 1
                if board[r] == 'OOO':
                    return -1
                if board[0][r] == 'X' and board[1][r] == 'X' and board[2][r] == 'X':
                    return 1
                if board[0][r] == 'O' and board[1][r] == 'O' and board[2][r] == 'O':
                    return -1
            if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
                return 1
            if board[2][0] == 'X' and board[1][1] == 'X' and board[0][2] == 'X':
                return 1
            if board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
                return -1
            if board[2][0] == 'O' and board[1][1] == 'O' and board[0][2] == 'O':
                return -1
            return 0
        O, X = 0, 0
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
        winner = Xwin(board)
        if winner == 1:
            return True if X - O == 1 else False
        elif winner == -1:
            return True if X - O == 0 else False
        return True
