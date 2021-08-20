def problem(a):
    if str(a).replace('.', '').isdigit() == True:
        a = a * 50 + 6
        return a
    else:
        return 'Error'
