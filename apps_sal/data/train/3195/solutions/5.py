def braces_status(string):
    s = "".join(list(filter(lambda ch: ch in "{[()]}", list(string))))
    while '{}' in s or '()' in s or '[]' in s:
        s = s.replace('{}', '')
        s = s.replace('[]', '')
        s = s.replace('()', '')
    return s == ''
