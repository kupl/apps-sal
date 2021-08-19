class Solution:

    def repeat(self, val, seen):
        print((val, seen))
        return seen >> int(val) & 1

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        seen = set()
        for i in range(9):
            for j in range(9):
                if board[i][j].isdigit():
                    val = board[i][j]
                    row = (i, val)
                    col = (val, j)
                    box = (i // 3, j // 3, val)
                    if row in seen or col in seen or box in seen:
                        return False
                    seen.add(row)
                    seen.add(col)
                    seen.add(box)
        return True
