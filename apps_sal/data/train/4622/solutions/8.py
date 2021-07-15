def double_check(strng):
    for idx in range(len(strng)-1):
        if strng[idx].lower() == strng[idx+1].lower():
            return True
    return False
