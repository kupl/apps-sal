class Solution:

    def movesToChessboard(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        N = len(board)
        for i in range(N):
            for j in range(N):
                if board[0][0] ^ board[0][j] ^ board[i][0] ^ board[i][j]:
                    return -1
        rowSum = 0
        colSum = 0
        rowSwap = 0
        colSwap = 0
        for i in range(N):
            rowSum += board[0][i]
            colSum += board[i][0]
            rowSwap += board[0][i] == i % 2
            colSwap += board[i][0] == i % 2
        if rowSum < N // 2 or rowSum > (N + 1) // 2:
            return -1
        if colSum < N // 2 or colSum > (N + 1) // 2:
            return -1
        if N % 2:
            if rowSwap % 2:
                rowSwap = N - rowSwap
            if colSwap % 2:
                colSwap = N - colSwap
        else:
            rowSwap = min(rowSwap, N - rowSwap)
            colSwap = min(colSwap, N - colSwap)
        return (rowSwap + colSwap) // 2
