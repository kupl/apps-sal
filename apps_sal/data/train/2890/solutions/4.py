def multiples(m, n):
    solution = []
    for i in range(1, m + 1):
        solution.insert(i, n * i)
    return solution
