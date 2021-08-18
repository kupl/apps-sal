def has_exit(board):
    def make(i, j, visited=None):
        if not visited:
            visited = []
        if [i, j] in visited or not (0 <= i < len(board) and 0 <= j < len(board[0])) or board[i][j] == "
        return False
        visited.append([i, j])
        if i == 0 or j == 0 or i == len(board) - 1 or j == len(board[0]) - 1:
            return True
        return any([make(i + 1, j, visited),
                    make(i - 1, j, visited),
                    make(i, j + 1, visited),
                    make(i, j - 1, visited)])
    li = [[i, k] for i, j in enumerate(board) for k, l in enumerate(j) if l == 'k']
    if len(li) > 1:
        raise
    return make(li[0][0], li[0][1])
