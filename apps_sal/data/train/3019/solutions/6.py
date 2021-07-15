def str_count(strng, letter):
    count = 0
    if letter in strng:
        for i in range(len(strng)):
            if strng[i] == letter:
                count += 1
        return count
    else:
        return 0
