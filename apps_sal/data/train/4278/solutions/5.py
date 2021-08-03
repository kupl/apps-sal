def diagonal(matrix):
    if sum(matrix[i][i] for i in range(len(matrix))) > sum(matrix[i][len(matrix) - 1 - i] for i in range(len(matrix))):
        return "Principal Diagonal win!"
    elif sum(matrix[i][i] for i in range(len(matrix))) < sum(matrix[i][len(matrix) - 1 - i] for i in range(len(matrix))):
        return "Secondary Diagonal win!"
    else:
        return "Draw!"
