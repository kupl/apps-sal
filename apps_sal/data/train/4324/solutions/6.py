def display_board(board, w):
    re = []
    for i in range(0, len(board), w):
        re.append('|'.join((' {} '.format(e) for e in board[i:i + w])))
    return ('\n' + '-' * len(re[0]) + '\n').join(re)
