def lowercase_count(strng):
    lst = list(strng)
    count = 0
    for letter in lst:
        if letter.islower():
            count += 1
    return count
