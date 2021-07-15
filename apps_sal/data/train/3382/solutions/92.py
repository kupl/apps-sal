def lowercase_count(strng):
    count = 0
    for char in strng:
        if char.islower() is True:
            count = count + 1
        else:
            continue
    return count
