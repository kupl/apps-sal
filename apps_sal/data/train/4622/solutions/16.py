def double_check(strng):
    for i in set(strng):
        if i*2 in strng.lower(): return True
    return False
