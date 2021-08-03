def double_check(strng):
    strng = strng.lower()
    l = []
    for x in strng:
        if x * 2 in strng:
            l.append(True)
    return bool(l)
