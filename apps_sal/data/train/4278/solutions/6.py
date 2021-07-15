def diagonal(matrix):
    principal_sum = sum(matrix[i][i] for i in range(len(matrix)))
    secondary_sum = sum(matrix[i][~i] for i in range(len(matrix)))
    if principal_sum > secondary_sum:
        return "Principal Diagonal win!"
    elif principal_sum < secondary_sum:
        return "Secondary Diagonal win!"
    else:
        return "Draw!"
