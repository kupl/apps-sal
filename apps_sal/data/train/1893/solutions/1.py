class Solution:

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row_dict = {}
        col_dict = {}
        ssq_dict = {}
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] != '.':
                    if 'r' + str(row) not in row_dict:
                        row_dict['r' + str(row)] = [board[row][col]]
                    else:
                        row_dict['r' + str(row)].append(board[row][col])
                    if 'c' + str(col) not in col_dict:
                        col_dict['c' + str(col)] = [board[row][col]]
                    else:
                        col_dict['c' + str(col)].append(board[row][col])
                    if 's' + str(row - row % 3) + str(col - col % 3) not in ssq_dict:
                        print('s' + str(row - row % 3) + str(col - col % 3))
                        ssq_dict['s' + str(row - row % 3) + str(col - col % 3)] = [board[row][col]]
                    else:
                        ssq_dict['s' + str(row - row % 3) + str(col - col % 3)].append(board[row][col])
        for val in row_dict.values():
            if len(val) > len(set(val)):
                return False
        for val in col_dict.values():
            if len(val) > len(set(val)):
                return False
        for val in ssq_dict.values():
            if len(val) > len(set(val)):
                return False
        return True
