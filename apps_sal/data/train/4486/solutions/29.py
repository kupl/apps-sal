def repeat_it(string, n):
    if type(string) == str:
        res = string * n
    else:
        res = 'Not a string'
    return res
