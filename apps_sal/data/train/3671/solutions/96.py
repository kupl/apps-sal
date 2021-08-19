def problem(a):
    if type(a) is str and a.isalpha():
        return 'Error'
    else:
        return a * 50 + 6
