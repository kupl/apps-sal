def lowercase_count(strng):
    li = list(strng)
    counter = 0
    for c in range(len(li)):
        if 96 < ord(li[c]) < 123:
            counter += 1
    return counter
