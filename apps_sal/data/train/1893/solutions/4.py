class Solution:

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        Cell = [[] for i in range(9)]
        Col = [[] for i in range(9)]
        Row = [[] for i in range(9)]
        for (i, row) in enumerate(board):
            for (j, num) in enumerate(row):
                if num != '.':
                    k = i // 3 * 3 + j // 3
                    if num in Row[i] + Col[j] + Cell[k]:
                        return False
                    Row[i].append(num)
                    Col[j].append(num)
                    Cell[k].append(num)
        return True
