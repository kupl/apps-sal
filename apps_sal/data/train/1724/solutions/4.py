def blast_sequence(aliens, shooter):
    (row, column) = (len(aliens[0]), shooter[0] + 1)
    board = [[0 for _ in range(row)] for _ in range(column)]
    for (i, j) in enumerate(aliens):
        board[i] = j
    find_pos = [[i, k, l] for (i, j) in enumerate(aliens) for (k, l) in enumerate(j) if l]

    def parse(x, y, z):
        c = 0
        while c < abs(z):
            if z > 0:
                y += 1
            else:
                y -= 1
            if y == row:
                x += 1
                (z, y) = (-z, row - 1)
            elif y == -1:
                x += 1
                (z, y) = (-z, 0)
            c += 1
        return [x, y, z]
    (turn, shoots) = (0, [])
    while find_pos and all((k[0] != shooter[0] for k in find_pos)):
        for (i, j) in enumerate(find_pos):
            find_pos[i] = parse(*j)
        targets = [k for k in find_pos if k[1] == shooter[1]]
        if targets:
            shoots.append(turn)
            find_pos.remove(max(targets, key=lambda x: (x[0], abs(x[2]), x[2])))
        turn += 1
    return [shoots, None][bool(find_pos)]
