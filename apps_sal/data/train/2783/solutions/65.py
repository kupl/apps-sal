def get_grade(*args):
    mean = sum(args) // len(args)
    print(mean)
    grade = 'F'
    if mean in range(60, 70):
        grade = 'D'
    if mean in range(70, 80):
        grade = 'C'
    if mean in range(80, 90):
        grade = 'B'
    if mean in range(90, 101):
        grade = 'A'
    return grade

