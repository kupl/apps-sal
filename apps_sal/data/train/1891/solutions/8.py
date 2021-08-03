class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        result = []
        visits = [0, 0, 0]
        board = [["." for j in range(n)] for i in range(n)]

        self.find(visits, n, 0, board, result)

        return result + [[row[:: -1] for row in board] for board in result if n & 1 == 0 or n & 1 == 1 and board[0][n >> 1] != "Q"]

    def find(self, visits, n, k, board, result):
        if k >= n:
            result.append(["".join(x for x in row) for row in board])
            return

        for j in range(n if k > 0 else n + 1 >> 1):
            if self.isInvalid(visits, k, j, n):
                continue

            self.toggleVisit(visits, k, j, n)
            board[k][j] = "Q"
            self.find(visits, n, k + 1, board, result)
            self.toggleVisit(visits, k, j, n)
            board[k][j] = "."

    def toggleVisit(self, visits, i, j, n):
        visits[0] ^= 1 << j
        visits[1] ^= 1 << i - j + n - 1
        visits[2] ^= 1 << i + j

    def isInvalid(self, visits, i, j, n):
        return visits[0] & (1 << j) > 0 or visits[1] & (1 << i - j + n - 1) > 0 or visits[2] & (1 << i + j) > 0
