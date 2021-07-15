def problem(a):
    if type(a) == int or type(a) == float:
        a *= 50
        a += 6
        return a
    else: 
        return 'Error';
