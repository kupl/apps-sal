def grader(score):
    return 'F' if score < 0.6 or score > 1 else ['D', 'C', 'B', 'A', 'A'][int(score * 10) - 6]
