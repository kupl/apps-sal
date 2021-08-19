def check_valid(letter_locations, board, word):
    if len(letter_locations) == len(word):
        return True
    (x, y) = letter_locations[-1]
    next_char = word[len(letter_locations)]
    valid = False
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if y + i < 0 or x + j < 0 or y + i >= len(board) or (x + j >= len(board[0])):
                continue
            if board[y + i][x + j] == next_char and (x + j, y + i) not in letter_locations:
                letter_locations.append((x + j, y + i))
                valid = valid or check_valid(letter_locations, board, word)
                letter_locations.pop()
    return valid


def find_word(board, word):
    valid = False
    if word == '':
        return True
    for (y, row) in enumerate(board):
        for (x, letter) in enumerate(row):
            if letter == word[0]:
                valid = valid or check_valid([(x, y)], board, word)
    return valid
