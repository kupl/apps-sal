def grader(score):
    return {'1': 'A', '0.9': 'A', '0.8': 'B', '0.7': 'C', '0.6': 'D'}.get(str(score)[:3], 'F')

