def grader(n):
    return 'F' if n > 1 or n < 0.6 else 'A' if n >= 0.9 else 'B' if n >= 0.8 else 'C' if n >= 0.7 else 'D'
