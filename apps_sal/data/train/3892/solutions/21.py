def grader(n):
    return 'FDCBAF'[(n >= 0.6) + (n >= 0.7) + (n >= 0.8) + (n >= 0.9) + (n > 1)]
