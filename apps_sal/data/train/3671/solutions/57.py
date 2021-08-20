def problem(a):
    if type(a) == type('s'):
        return 'Error'
    else:
        return a * 50 + 6


print(problem('jf'))
