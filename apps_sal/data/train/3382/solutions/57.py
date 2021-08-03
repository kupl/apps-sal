def lowercase_count(strng):

    nb = 0

    for ch in strng:
        if ch.islower():
            nb += 1

    return nb
