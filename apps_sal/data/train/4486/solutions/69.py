def repeat_it(string,n):
    if not isinstance(string, str):
        return "Not a string"
    return ''.join(string for i in range(n))
