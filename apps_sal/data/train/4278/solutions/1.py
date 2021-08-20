def diagonal(matrix):
    (sp, ss) = map(sum, zip(*((matrix[x][x], matrix[len(matrix) - 1 - x][x]) for x in range(len(matrix)))))
    return 'Draw!' if ss == sp else '{} Diagonal win!'.format('Principal' if sp > ss else 'Secondary')
