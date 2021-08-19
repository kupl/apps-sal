def problem(a):
    if type(a) == str:
        return 'Error'
    elif type(a) is not str:
        return a * 50 + 6
