def score_matrix(matrix):
    total_sum = 0
    for (x,row) in enumerate(matrix):
        for (y, v) in enumerate(row):
            total_sum += v * (1 if (x+y)%2 == 0 else -1)
    return total_sum
