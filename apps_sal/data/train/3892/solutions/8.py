scores = ((1.01, 'F'), (0.9, 'A'), (0.8, 'B'), (0.7, 'C'), (0.6, 'D'), (0, 'F'))


def grader(score):
    return [grade for (t, grade) in scores if score >= t][0]
