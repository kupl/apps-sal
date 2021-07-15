def str_count(strng, letter):
    count = 0
    i = 0
    if len(strng) == 0:
        return count
    else:
        for letters in strng:
            if strng[i] == letter[0]:
                count += 1
                i += 1
            else:
                i += 1
        return count
