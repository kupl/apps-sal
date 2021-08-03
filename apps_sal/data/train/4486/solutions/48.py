def repeat_it(string, n):
    print(string, n)
    if string == str(string):
        return string * n if string else 'Not a string'
    else:
        return 'Not a string'
