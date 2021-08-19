import time


def count(board):
    N = len(board)
    dp = board
    size_cnt = {}
    for row in range(1, N):
        for col in range(1, N):
            if board[row][col] == 1:
                size = 1 + min(dp[row - 1][col - 1], min(dp[row - 1][col], dp[row][col - 1]))
                dp[row][col] = size
                if size > 1:
                    size_cnt[size] = size_cnt.get(size, 0) + 1
    res = {}
    for k in size_cnt:
        for s in range(2, k + 1):
            res[s] = res.get(s, 0) + size_cnt[k]
    return res
