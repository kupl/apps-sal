def problem(a):
    if type(a) == int:
        a = a*50+6
        return a
    elif type(a) == float:
        a = a*50+6
        return int(a)
    else:
        return "Error"
