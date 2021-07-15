def repeat_it(string,n):
    return str(string*n if isinstance(string, str) else 'Not a string')
