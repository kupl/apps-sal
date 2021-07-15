def str_count(strng, letter):
    count = 0
    for letr in strng:
        if letter == letr: count += 1
        else: count += 0
    return count
