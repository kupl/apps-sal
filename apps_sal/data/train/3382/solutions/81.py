def lowercase_count(strng):
    counter = 0
    for el in strng:
        if el in "qwertyuiopasdfghjklzxcvbnm":
            counter += 1
    return counter
