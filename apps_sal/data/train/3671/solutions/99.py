def problem(a):
    a = str(a)
    return "Error" if a.isalpha() else 50 * eval(a) + 6
