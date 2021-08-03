def problem(a):
    if type(a) == type('str'):
        return 'Error'
    elif type(a) == type(19) or type(9.3):
        return (a * 50) + 6
    else:
        return 'Error'
