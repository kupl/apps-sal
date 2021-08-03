class Solution:
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        o_cnt = 0
        x_cnt = 0

        bingo_x = 0
        bingo_o = 0

        for i in range(3):
            if board[i] == 'O' * 3:
                bingo_o += 1
            if board[i] == 'X' * 3:
                bingo_x += 1

            if board[0][i] == board[1][i] == board[2][i]:
                if board[0][i] == 'O':
                    bingo_o += 1
                if board[0][i] == 'X':
                    bingo_x += 1

            for j in range(3):
                if board[i][j] == 'O':
                    o_cnt += 1
                elif board[i][j] == 'X':
                    x_cnt += 1

        if x_cnt < o_cnt:
            return False
        elif x_cnt - o_cnt > 1:
            return False

        if board[1][1] == board[0][2] == board[2][0]:
            if board[1][1] == 'O':
                bingo_o += 1
            elif board[1][1] == 'X':
                bingo_x += 1

        if board[0][0] == board[1][1] == board[2][2]:
            if board[0][0] == 'O':
                bingo_o += 1
            elif board[0][0] == 'X':
                bingo_x += 1

        if bingo_x >= 1 and bingo_o >= 1:
            return False

        if bingo_x >= 1:
            return x_cnt == (o_cnt + 1)
        elif bingo_o >= 1:
            return x_cnt == o_cnt

        return True
