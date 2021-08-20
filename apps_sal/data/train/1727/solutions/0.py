def find_word(board, word):
    grid = [l + [''] for l in board] + [[''] * (len(board[0]) + 1)]

    def rc(x, y, i):
        if i == len(word):
            return True
        if grid[x][y] != word[i]:
            return False
        grid[x][y] = ''
        r = any((rc(x + u, y + v, i + 1) for u in range(-1, 2) for v in range(-1, 2)))
        grid[x][y] = word[i]
        return r
    return any((rc(x, y, 0) for x in range(len(board)) for y in range(len(board[x]))))
