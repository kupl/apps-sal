def str_count(strng, letter):
    count = 0
    for i in strng:
        if i == letter:
            count += 1
    return count
