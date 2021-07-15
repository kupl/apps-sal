def str_count(strng, letter):
    count = 0
    for i in range(len(strng)):
        if strng[i] == letter[0]:
            count += 1
    return count
