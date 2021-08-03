def remove_chars(s):
    for x in s:
        if x != ' ':
            if not x.isalpha():
                s = s.replace(x, '')
    return s
