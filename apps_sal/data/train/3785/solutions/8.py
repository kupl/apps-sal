def generate_diagonal(n, l):
    row = [1]
    for k in range(1, l):
        row.append(row[-1] * (n + k) // k)
    return row if l else []
