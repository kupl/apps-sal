def repeat_it(string, n):
    try:
        a = string.lower()
        return string * n
    except:
        return 'Not a string'
