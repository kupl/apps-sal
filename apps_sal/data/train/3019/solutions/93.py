def str_count(strng, letter):
    total = 0
    for i in range(len(strng)):
        if strng[i] == letter:
            total += 1
    return total
