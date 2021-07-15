def repeat_it(string,n):
    return ''.join(string for i in range(n)) if type(string) == str else 'Not a string'
