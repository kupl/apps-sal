class Solution:
    full_values = set('123456789')

    def findValues(self, board, row, col):
        row_start = row // 3 * 3
        col_start = col // 3 * 3
        values = self.full_values - (set(board[row]) | {board[i][col] for i in range(9)} | {board[i][j] for i in range(row_start, row_start + 3) for j in range(col_start, col_start + 3)})
        return values

    def solver(self, board):
        done = True
        for row in board:
            if '.' in row:
                done = False
        if done:
            return True
        row_num = len(board)
        col_num = len(board[0])
        candidates = [[0 for x in range(row_num)] for y in range(col_num)]
        NumOfCandidatesDict = [[] for i in range(9)]
        for row in range(row_num):
            for col in range(col_num):
                if board[row][col] == '.':
                    candidates[row][col] = self.findValues(board, row, col)
                    if len(candidates[row][col]) == 0:
                        return False
                    elif len(candidates[row][col]) == 1:
                        board[row][col] = candidates[row][col].pop()
                        ret = self.solver(board)
                        if ret:
                            return True
                        else:
                            board[row][col] = '.'
                            return False
                    else:
                        NumOfCandidatesDict[len(candidates[row][col])].append([row, col])
        for i in range(2, 10):
            if len(NumOfCandidatesDict[i]) > 0:
                (row, col) = NumOfCandidatesDict[i][0]
                for value in candidates[row][col]:
                    board[row][col] = value
                    if self.solver(board):
                        return True
                board[row][col] = '.'
                return False
        return False

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.solver(board)
