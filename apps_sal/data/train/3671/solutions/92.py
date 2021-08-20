def problem(a):
    is_string = isinstance(a, str)
    if is_string == True:
        return 'Error'
    else:
        return a * 50 + 6
