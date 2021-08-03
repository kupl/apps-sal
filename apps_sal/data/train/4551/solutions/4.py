def score_matrix(m): return sum(y * [1, -1][(i + j) & 1] for i, x in enumerate(m) for j, y in enumerate(x))
