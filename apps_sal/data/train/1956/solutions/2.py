class Solution(object):

    def __init__(self):
        self.filled = []

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        pln = []
        for i in range(9):
            pln.append([])
            self.filled.append([])
            for j in range(9):
                if board[i][j].isdigit():
                    self.filled[-1].append(True)
                    pln[i].append([])
                else:
                    self.filled[-1].append(False)
                    pln[i].append([k for k in range(10)])
                    pln[i][-1].remove(0)
        for i in range(9):
            for j in range(9):
                if board[i][j].isdigit():
                    self.updatePln(pln, int(board[i][j]), i, j)
        result = self.loopSolution(pln, board)
        return

    def updatePln(self, pln, temp, i, j):
        for k in range(9):
            a = pln[i][k]
            if temp in pln[i][k]:
                pln[i][k].remove(temp)
            if temp in pln[k][j]:
                pln[k][j].remove(temp)
            num = int(i / 3) * 3 + int(j / 3)
            if temp in pln[int(num / 3) * 3 + int(k / 3)][num % 3 * 3 + k % 3]:
                pln[int(num / 3) * 3 + int(k / 3)][num % 3 * 3 + k % 3].remove(temp)

    def loopSolution(self, pln, board):
        while True:
            (row, column, minSize) = (10, 10, 10)
            for i in range(9):
                for j in range(9):
                    if not self.filled[i][j] and len(pln[i][j]) == 0:
                        return False
                    if len(pln[i][j]) > 0 and len(pln[i][j]) < minSize:
                        (row, column) = (i, j)
                        minSize = len(pln[i][j])
            if minSize == 10:
                return True
            else:
                for i in range(minSize):
                    self.filled[row][column] = True
                    temp_pln = []
                    for ele in pln:
                        temp_pln.append([])
                        for ele2 in ele:
                            temp_pln[-1].append(ele2[:])
                    self.updatePln(temp_pln, temp_pln[row][column][i], row, column)
                    temp_pln[row][column] = []
                    if self.loopSolution(temp_pln, board):
                        board[row][column] = str(pln[row][column][i])
                        return True
                    self.filled[row][column] = False
                return False
