class Solution:
    def movesToChessboard(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        n = len(board)
        for i in range(1, n):
            for j in range(1, n):
                if (board[0][0] + board[0][j] + board[i][0] + board[i][j]) % 2 != 0:
                    return -1
        result = 0
        x = 0
        y = 0
        for i in range(0, n):
            if i % 2 == 0 and board[i][0] == 1:
                x += 1
            elif i % 2 == 1 and board[i][0] == 0:
                y += 1
        if n % 2 == 0:
            if x != y:
                return -1
            result += min(x, n // 2 - x)
        else:
            if x == y:
                result += x
            elif (n + 1) // 2 - x == (n - 1) // 2 - y:
                result += (n + 1) // 2 - x
            else:
                return -1
        x = 0
        y = 0
        for i in range(0, n):
            if i % 2 == 0 and board[0][i] == 1:
                x += 1
            elif i % 2 == 1 and board[0][i] == 0:
                y += 1
        if n % 2 == 0:
            if x != y:
                return -1
            result += min(x, n // 2 - x)
        else:
            if x == y:
                result += x
            elif (n + 1) // 2 - x == (n - 1) // 2 - y:
                result += (n + 1) // 2 - x
            else:
                return -1
        return result
