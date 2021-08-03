def grader(s):
    print(s)
    if s > 1 or s < .6:
        return "F"
    if s >= .9:
        return "A"
    if s >= .8:
        return "B"
    if s >= .7:
        return "C"
    return "D"
