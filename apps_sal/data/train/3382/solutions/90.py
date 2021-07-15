def lowercase_count(strng):
    count = 0
    for x in strng:
        if x.islower():
            count += 1
    else:
        return count
