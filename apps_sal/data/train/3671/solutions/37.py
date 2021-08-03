def problem(value):
    try:
        int(value)
    except:
        return 'Error'
    return value * 50 + 6
