def str_count(strng, letter):
    k = 0
    for i in strng:
        if letter == i:
            k += 1
    return k
