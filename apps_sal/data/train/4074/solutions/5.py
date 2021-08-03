def between_extremes(numbers):
    a, *b, c = sorted(numbers)
    return c - a
