def grader(s):
    return 'F' if s < 0.6 or s > 1 else 'A' if s >= 0.9 else 'B' if s >= 0.8 else 'C' if s >= 0.7 else 'D' if s >= 0.6 else 'F'
