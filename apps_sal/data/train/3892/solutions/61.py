def grader(score):
    print(score)
    return {0.6: 'D', 0.7: 'C', 0.8: 'B', 0.9: 'A', 1:'A', 1.1: 'F'}.setdefault(score, 'F')

