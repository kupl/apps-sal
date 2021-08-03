def problem(a):
    if type(a) == float:
        return a * 50 + 6
    elif type(a) != int:
        return "Error"
    else:
        return a * 50 + 6
