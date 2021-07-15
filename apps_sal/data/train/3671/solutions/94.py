def problem(a):
    print(a, type(a))
    return a * 50 + 6 if isinstance(a, int) or isinstance(a, float) else 'Error'
