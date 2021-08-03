from collections import defaultdict


def count(chessBoard):
    n, result = len(chessBoard), defaultdict(int)
    memo = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if chessBoard[i - 1][j - 1]:
                memo[i][j] = min(memo[i - 1][j], memo[i][j - 1], memo[i - 1][j - 1]) + 1
                for x in range(2, memo[i][j] + 1):
                    result[x] += 1
    return result
