def lowercase_count(strng):
    count = 0
    for chr in strng:
        if chr != chr.upper():
            count += 1
    return count
