def grader(input):
    if input > 1 or input < 0.6:
        return "F"
    elif input >= 0.9:
        return "A"
    elif input >= 0.8:
        return "B"
    elif input >= 0.7:
        return "C"
    else:
        return "D"
