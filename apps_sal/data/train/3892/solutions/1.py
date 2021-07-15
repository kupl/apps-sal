def grader(score):
    for limit, grade in [(0.9, "A"), (0.8, "B"), (0.7, "C"), (0.6, "D")]:
        if limit <= score <= 1:
            return grade
    return 'F'

