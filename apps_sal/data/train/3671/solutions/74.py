def problem(a):
    print(a)
    try:
        return float(a) * 50 + 6
    except ValueError:
        return 'Error'
