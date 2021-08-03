def grader(x):
    if 0.9 <= x <= 1:
        return "A"
    elif 0.8 <= x < 0.9:
        return "B"
    elif 0.7 <= x < 0.8:
        return "C"
    elif 0.6 <= x < 0.7:
        return "D"
    else:
        return "F"
