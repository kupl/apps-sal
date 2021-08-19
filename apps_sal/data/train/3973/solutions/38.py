def remove_char(s):
    if len(s) < 2:
        return s
    else:
        n = len(s) - 1
        return s[1:n]
