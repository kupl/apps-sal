def repeat_it(string, n):
    if type(string) == int:
        return 'Not a string'
    elif not string:
        return 'Not a string'
    try:
        for char in string:
            if char == '2':
                return string * n
            elif char.isdigit():
                return 'Not a string'
        return string * n
    except:
        return 'Not a string'
