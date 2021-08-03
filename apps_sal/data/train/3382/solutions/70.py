def lowercase_count(strng):
    sum = 0
    for i in range(len(strng)):
        if strng[i].islower() == True:
            sum += 1

    return sum
