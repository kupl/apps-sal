def leaderboard_sort(board, changes):
    for i, e in enumerate(changes):
        name, point = e.split()
        l = board.index(name)
        board.insert( int(eval(f'{l}-({point})')), board.pop(l))
    return board

