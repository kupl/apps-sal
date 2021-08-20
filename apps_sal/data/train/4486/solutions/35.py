def repeat_it(string, n):
    return string * n if str(n).isdigit() and isinstance(string, str) else 'Not a string'
