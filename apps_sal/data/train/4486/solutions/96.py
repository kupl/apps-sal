def repeat_it(string, n):
    return 'Not a string' if not isinstance(string, str) else string + repeat_it(string, n - 1) if n else ''
