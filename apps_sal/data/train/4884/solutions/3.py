def connect_the_dots(paper):
    board = list(map(list, paper.splitlines(keepends=True)))
    alphabets = {
        x: (i, j)
        for i, row in enumerate(board)
        for j, x in enumerate(row)
        if not x.isspace()
    }
    coords = [coord for _, coord in sorted(alphabets.items())]
    for (r1, c1), (r2, c2) in zip(coords, coords[1:]):
        dr = 0 if r1 == r2 else (r2 - r1) // abs(r2 - r1)
        dc = 0 if c1 == c2 else (c2 - c1) // abs(c2 - c1)
        while True:
            board[r1][c1] = '*'
            if r1 == r2 and c1 == c2:
                break
            r1 += dr
            c1 += dc
    return ''.join(map(''.join, board))
