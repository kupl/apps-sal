from collections import defaultdict


def count(chessBoard):
    n, ans = len(chessBoard), defaultdict(int)
    grid = [[0] * (n + 1) for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if(chessBoard[i - 1][j - 1] != 0):
                grid[i][j] = min(grid[i - 1][j], grid[i][j - 1], grid[i - 1][j - 1]) + 1
                for x in range(2, grid[i][j] + 1):
                    ans[x] += 1
    return(ans)
