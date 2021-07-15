def find_neighbors(row_c, col_c, board, word, path):
    if len(path) == len(word):
        return True, path
    y_d = [i for i in range(max(0, row_c - 1), min(len(board), row_c + 2))]
    x_d = [i for i in range(max(0, col_c - 1), min(len(board), col_c + 2))]
    neighbors = [(y, x) for y in y_d for x in x_d]
    for index in neighbors:
        if index not in path and board[index[0]][index[1]] == word[len(path)]:
            path.append(index)
            result = find_neighbors(index[0], index[1], board, word, path)
            if result[0]:
                return True, path
            else:
                path = result[1]
            path = path[:-1]
    return False, path


def find_word(board, word):
    for row_c, row in enumerate(board):
        for col_c, l in enumerate(row):
            path = []
            if l in word and find_neighbors(row_c, col_c, board, word, path)[0]:
                return True
    return False
