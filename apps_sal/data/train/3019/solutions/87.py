def str_count(strng, letter):
    j = 0
    for i in range(0, len(strng)):
        if strng[i] == letter:
            j += 1
    return j
