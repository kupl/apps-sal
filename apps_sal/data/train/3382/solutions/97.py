def lowercase_count(strng):
    count = 0
    for el in strng:
        count = count + (1 if el != el.upper() else 0)
    return count
