def grader(score):
    if score < 0.6:
        return 'F'
    elif score < 0.7:
        return 'D'
    elif score < 0.8:
        return "C"
    elif score < 0.9:
        return "B"
    elif score <= 1:
        return "A"
    elif score > 1:
        return "F"
    else:
        None
    print(grader(score))
