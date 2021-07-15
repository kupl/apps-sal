def lowercase_count(strng):
    lc = 0
    for letter in strng:
        if 'z' >= letter >= 'a':
            lc += 1
    return lc
