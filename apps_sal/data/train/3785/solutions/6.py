def generate_diagonal(n, l):
    # return an array containing the numbers in the nth diagonal of Pascal's triangle, to the specified length
    if l == 0:
        return []
    diagonal = [1]
    for i in range(l)[1:]:
        diagonal.append(diagonal[-1] * (n + i) / i)
    return diagonal
