def problem(a):
    if isinstance(a, str):
        return 'Error'
    else:
        return int(a * 50 + 6)
