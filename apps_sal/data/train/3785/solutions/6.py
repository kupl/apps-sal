def generate_diagonal(n, l):
    if l == 0:
        return []
    diagonal = [1]
    for i in range(l)[1:]:
        diagonal.append(diagonal[-1] * (n + i) / i)
    return diagonal
