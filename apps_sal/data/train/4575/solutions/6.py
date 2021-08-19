def smallest_integer(matrix):
    numbers = sorted(set((n for row in matrix for n in row if n >= 0)))
    return next((b for (a, b) in zip(numbers, range(len(numbers))) if a != b), len(numbers))
