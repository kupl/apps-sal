class Solution:

    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        num_X = 0
        num_O = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == 'X':
                    num_X += 1
                elif board[i][j] == 'O':
                    num_O += 1
        if num_X < num_O or num_X > num_O + 1:
            return False

        def win(board, total_X, total_O):
            for i in range(3):
                num_X = 0
                num_O = 0
                for j in range(3):
                    if board[i][j] == 'X':
                        num_X += 1
                    elif board[i][j] == 'O':
                        num_O += 1
                if num_X == 3:
                    return total_X > total_O
                if num_O == 3:
                    return total_X == total_O
            for j in range(3):
                num_X = 0
                num_O = 0
                for i in range(3):
                    if board[i][j] == 'X':
                        num_X += 1
                    elif board[i][j] == 'O':
                        num_O += 1
                if num_X == 3:
                    return total_X > total_O
                if num_O == 3:
                    return total_X == total_O
            num_X = 0
            num_O = 0
            for i in range(3):
                if board[i][i] == 'X':
                    num_X += 1
                elif board[i][i] == 'O':
                    num_O += 1
            if num_X == 3:
                return total_X > total_O
            if num_O == 3:
                return total_X == total_O
            num_X = 0
            num_O = 0
            for i in range(3):
                if board[i][2 - i] == 'X':
                    num_X += 1
                elif board[i][2 - i] == 'O':
                    num_O += 1
            if num_X == 3:
                return total_X > total_O
            if num_O == 3:
                return total_X == total_O
            return True
        return win(board, num_X, num_O)
