def string_clean(s):
    string = ''
    for char in s:
        if char not in '0123456789':
            string += char
    return string
