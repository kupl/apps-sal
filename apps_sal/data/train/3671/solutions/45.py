def problem(a=''):
    try:
        int(a)
        a = a * 50 + 6
        return a
    except ValueError:
        return "Error"
