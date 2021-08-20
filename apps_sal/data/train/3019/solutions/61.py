def str_count(strng, letter):
    count = 0
    for check in strng:
        if check == letter:
            count += 1
    return count
