def lowercase_count(strng):
    lower = 0
    for letter in strng:
        if letter >= 'a' and letter <= 'z':
            lower += 1
    return lower
