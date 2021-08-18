def remove_chars(s):
    ret = ''
    for c in s:
        if c.isalpha() or c is ' ':
            ret += c
    return ret
