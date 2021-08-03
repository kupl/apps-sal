def repeat_it(string, n):
    return (string + repeat_it(string, n - 1) if n > 0 else "") if type(string) is str else "Not a string"
