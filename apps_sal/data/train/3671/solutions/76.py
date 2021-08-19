def problem(a):
    print(a)
    return a * 50 + 6 if not isinstance(a, str) else 'Error'
