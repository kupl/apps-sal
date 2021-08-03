def grader(score):
    import math
    grade = 9 - int(math.ceil(score * 10))
    if grade < -1 or grade > 4:
        grade = 4
    return ['A', 'B', 'C', 'D', 'F', 'A'][grade]
