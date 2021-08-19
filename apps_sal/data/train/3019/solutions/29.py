def str_count(strng, letter):
    count = 0
    for alphabet in strng:
        if letter == alphabet:
            count += 1
    return count
