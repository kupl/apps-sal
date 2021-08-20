def problem(a):
    try:
        if type(a) != str:
            return a * 50 + 6
        else:
            return 'Error'
    except ValueError:
        return 'Error'
