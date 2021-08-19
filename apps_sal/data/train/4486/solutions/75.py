def repeat_it(string, n):
    if type(string) is not str:
        return 'Not a string'
    result = ''
    for _ in range(0, n):
        result += string
    return result
