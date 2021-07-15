def problem(a):
    try:
        return a * 50 + 6
    except TypeError as e:
        return 'Error'
