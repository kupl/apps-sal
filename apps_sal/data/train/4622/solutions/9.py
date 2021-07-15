def double_check(strng):
    c_ = None
    for c in strng.upper():
        if c == c_: return True
        c_ = c
    return False
