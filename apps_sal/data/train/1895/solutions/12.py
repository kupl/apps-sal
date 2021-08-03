class Solution:
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        valid_X, valid_O = 0, 0
        cnt_X, cnt_O = 0, 0
        # for i in range (3):
        #     if board[i] == 'OOO' or board[i] =='XXX':
        #         valid_row += 1
        #     cnt_X += board[i].count('X')
        #     cnt_O += board[i].count('O')
        # sum_row = sum(valid_row)
        for row in board:
            if row == 'XXX':
                valid_X += 1
            elif row == 'OOO':
                valid_O += 1
            cnt_X += row.count('X')
            cnt_O += row.count('O')

        a, b, c = board
        for col in zip(a, b, c):
            if col == 'XXX':
                valid_X += 1
            elif col == 'OOO':
                valid_O += 1
        if board[1][1] != ' ':
            if board[0][0] == board[2][2] == board[1][1]:
                if board[1][1] == 'X':
                    valid_X += 1
                else:
                    valid_O += 1

            if board[2][0] == board[0][2] == board[1][1]:
                if board[1][1] == 'X':
                    valid_X += 1
                else:
                    valid_O += 1

        if valid_X + valid_O > 1:
            return False
        if valid_X:
            if cnt_X - cnt_O != 1:
                return False
        elif valid_O:
            if cnt_X != cnt_O:
                return False
        else:
            if not (0 <= cnt_X - cnt_O <= 1):
                return False
        return True
