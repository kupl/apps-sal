class Solution:

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = []
        cols = []
        squares = []
        for i in range(0, len(board)):
            rows.append(set())
            cols.append(set())
            squares.append(set())
        for i in range(0, len(board)):
            for j in range(0, len(board)):
                if board[i][j] == '.':
                    continue
                val = board[i][j]
                if val in rows[i]:
                    return False
                rows[i].add(val)
                if val in cols[j]:
                    return False
                cols[j].add(val)
                sq = int(i // 3) * 3
                sq += int(j // 3)
                print(('row is: ', i, ' col is: ', j, ' sq is: ', sq))
                if val in squares[sq]:
                    return False
                squares[sq].add(val)
        return True
