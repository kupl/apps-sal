def double_check(strng):
    for i in set(strng.lower()):
        if strng.lower().count(i*2)>=1:
            return True
    return False

