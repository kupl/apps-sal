def lowercase_count(strng):
    i = 0
    for x in strng:
        if 'a' <= x <= 'z':
            i += 1
    return i
