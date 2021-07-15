def lowercase_count(strng):
    count = 0
    for i in strng:
        if i.lower() == i and i.isalpha():
            count += 1
    return count
