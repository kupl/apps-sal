def lowercase_count(strng):

    lowerCastCount = 0

    for i in strng:

        if i.isdigit():
            None
        else:
            if i.islower():
                lowerCastCount += 1

    return lowerCastCount
