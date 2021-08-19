class Solution:
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        x_count, o_count = 0, 0
        # Count number of X and O
        for string in board:
            for c in string:
                if c == "X":
                    x_count += 1
                if c == "O":
                    o_count += 1
        # If number of X is two more than or less than that of O, return False
        if x_count - o_count >= 2 or x_count - o_count < 0:
            return False

        # Check winner, we can only have one winner. To check winner,
        # there are total 8 combinations.
        x_win = 0
        o_win = 0
        if board[0] == 'XXX' or board[1] == 'XXX' or board[2] == 'XXX':
            x_win += 1
        if board[0] == 'OOO' or board[1] == 'OOO' or board[2] == 'OOO':
            o_win += 1
        if board[0][0] + board[1][0] + board[2][0] == 'XXX' or \
                board[0][1] + board[1][1] + board[2][1] == 'XXX' or \
                board[0][2] + board[1][2] + board[2][2] == 'XXX':
            x_win += 1
        if board[0][0] + board[1][0] + board[2][0] == 'OOO' or \
                board[0][1] + board[1][1] + board[2][1] == 'OOO' or \
                board[0][2] + board[1][2] + board[2][2] == 'OOO':
            o_win += 1
        if board[0][0] + board[1][1] + board[2][2] == 'XXX' or \
                board[2][0] + board[1][1] + board[0][2] == 'XXX':
            x_win += 1
        if board[0][0] + board[1][1] + board[2][2] == 'OOO' or \
                board[2][0] + board[1][1] + board[0][2] == 'OOO':
            o_win += 1

        if x_win == 1 and o_win == 1:
            return False
        if x_win == 1 and x_count - o_count != 1 or \
                o_win == 1 and o_count != x_count:
            return False
        return True
