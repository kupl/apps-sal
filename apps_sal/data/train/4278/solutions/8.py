def diagonal(matrix):
    primary = sum((matrix[i][i] for i in range(len(matrix))))
    secondary = sum((matrix[i][len(matrix) - i - 1] for i in range(len(matrix))))
    return ['Principal Diagonal win!', 'Secondary Diagonal win!', 'Draw!'][0 if primary > secondary else 1 if primary < secondary else 2]
