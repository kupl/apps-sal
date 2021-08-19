def str_count(strng, letter):
    count = 0
    for item in strng:
        if item in letter:
            count += 1
    return count
