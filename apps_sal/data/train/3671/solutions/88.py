def problem(a):
    if type(a) == int or type(a) == float:
        return int((a * 50) + 6)
    else:
        return 'Error'

print(problem(1.2))
