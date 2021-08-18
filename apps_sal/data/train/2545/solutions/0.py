class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        count = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'R':
                    d = 1
                    while 0 <= i - d:
                        if board[i - d][j] == 'B':
                            break
                        elif board[i - d][j] == 'p':
                            count += 1
                            break
                        else:
                            d += 1
                    d = 1
                    while i + d <= len(board) - 1:
                        if board[i + d][j] == 'B':
                            break
                        elif board[i + d][j] == 'p':
                            count += 1
                            break
                        else:
                            d += 1
                    d = 1
                    while 0 <= j - d:
                        if board[i][j - d] == 'B':
                            break
                        elif board[i][j - d] == 'p':
                            count += 1
                            break
                        else:
                            d += 1
                    d = 1
                    while j + d <= len(board[i]) - 1:
                        if board[i][j + d] == 'B':
                            break
                        elif board[i][j + d] == 'p':
                            count += 1
                            break
                        else:
                            d += 1
        return count
