def grader(s):
    return 'ABCDF'[int(10 * (0.99 - s))] if s <= 1 and s > 0.4 else 'F'
