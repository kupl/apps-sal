def repeat_it(string, n):
    result = ''
    if type(string) != type('string'):
        return 'Not a string'
    else:
        result += string * n
    return result
