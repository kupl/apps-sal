def lowercase_count(strng):
    lowers = 'abcdefghijklmnopqrstuvwxyz'
    count = 0
    for c in strng:
        if c in lowers: count += 1
    return count
