def remove_chars(s):
    # without importing string or re and using a quick logic loop
    ret = ''
    for c in s:
        if c.isalpha() or c is ' ':
            ret += c
    return ret
