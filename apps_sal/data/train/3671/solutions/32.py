def problem(a):
    try:
        if a != str:
            return a * 50 + 6
    except TypeError:
        return 'Error'
