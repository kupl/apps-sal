def grader(score):
    if score > 1:
        return 'F'
    for (s, g) in [(0.9, 'A'), (0.8, 'B'), (0.7, 'C'), (0.6, 'D')]:
        if score >= s:
            return g
    return 'F'
