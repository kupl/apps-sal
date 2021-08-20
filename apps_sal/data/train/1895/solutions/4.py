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
        if X - O == 0:
            for r in board:
                if r == 'XXX':
                    return False
            for c in range(2):
                if board[0][c] == board[1][c] == board[2][c] == 'X':
                    return False
            if board[0][0] == board[1][1] == board[2][2] == 'X':
                return False
            if board[2][0] == board[1][1] == board[0][2] == 'X':
                return False
        else:
            for r in board:
                if r == 'OOO':
                    return False
            for c in range(2):
                if board[0][c] == board[1][c] == board[2][c] == 'O':
                    return False
            if board[0][0] == board[1][1] == board[2][2] == 'O':
                return False
            if board[2][0] == board[1][1] == board[0][2] == 'O':
                return False
        return True
