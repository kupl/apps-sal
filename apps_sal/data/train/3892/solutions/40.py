def grader(input, grades=("A", "B", "C", "D")):
    if input > 1:
        return "F"
    for i, x in enumerate(grades):
        if input >= (0.9 - 0.1 * i):
            return x
    return "F"
