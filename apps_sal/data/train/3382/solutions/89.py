def lowercase_count(strng):
    letters = list(strng)
    count = 0
    for i in letters:
        if ord(i) > 96 and ord(i) < 123:
            count += 1   
    return count
