def problem(a):
    try:
        return (a + 0) * 50 + 6
    except TypeError:
        return 'Error'
