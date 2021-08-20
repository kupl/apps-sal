qualification = {1: 'A', 0.9: 'A', 0.8: 'B', 0.7: 'C', 0.6: 'D'}


def grader(score):
    if score in qualification:
        return qualification.get(score)
    return 'F'
