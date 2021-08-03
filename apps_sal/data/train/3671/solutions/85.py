def problem(a):
    str_ref = isinstance(a, str)
    if str_ref is True:
        return "Error"
    else:
        return a * 50 + 6
