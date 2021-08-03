scores = ((1.01, 'F'), (.9, 'A'), (.8, 'B'), (.7, 'C'), (.6, 'D'), (0, 'F'))


def grader(score):
    return [grade for t, grade in scores if score >= t][0]
