def find_word(board, word):
    def make(i, j, string, f=1, visited=None):
        if not visited : visited = []
        visited = [[k, l] for k, l in visited if board[k][l] in string]
        if [i, j] in visited or not word.startswith(string): return False
        if not f:
            if 0 <= i < len(board) and 0 <= j < len(board) : string += board[i][j]
            else : return string == word
        if string == word : return True
        visited.append([i, j])
        return any([make(i, j + 1, string, 0, visited),
                    make(i, j - 1, string, 0, visited),
                    make(i - 1, j, string, 0, visited),
                    make(i + 1, j, string, 0, visited),
                    make(i - 1, j + 1, string, 0, visited),
                    make(i - 1, j - 1, string, 0, visited),
                    make(i + 1, j + 1, string, 0, visited),
                    make(i + 1, j - 1, string, 0, visited)])
    return any(make(i, k, l) for i, j in enumerate(board) for k, l in enumerate(j) if l == word[0])
