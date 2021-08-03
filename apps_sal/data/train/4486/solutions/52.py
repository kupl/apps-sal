def repeat_it(string, n):
    if not isinstance(string, str):
        return "Not a string"
    result = ''
    for s in range(0, n):
        result += string
    return result
