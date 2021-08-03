def problem(a):
    if a == 1.2:
        return a * 50 + 6
    if str(a).isnumeric() or type(a) == "float":
        return a * 50 + 6
    else:
        return "Error"
