def grader(input):
    import math
    return ['F', 'D', 'C', 'B', 'A'][min(max(math.trunc(input * 10) - 5, 0), 4)] if input <= 1 else 'F'
