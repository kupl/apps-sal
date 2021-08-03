def lowercase_count(strng):
    n = 0
    for k in strng:
        if k.islower():
            n += 1
    return n
