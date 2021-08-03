def double_check(str):
    str = str.lower()
    c1 = ''
    for c in str:
        if c == c1:
            return True
        c1 = c
    return False
