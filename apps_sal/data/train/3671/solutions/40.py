def problem(a):
    if type(a).__name__ != 'str':
        return a * 50 + 6
    else:
        return 'Error'
