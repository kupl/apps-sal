def remove_chars(s):
    w = ''
    for c in s:
        if c.isalpha() or c == ' ':
            w += c
    return w
