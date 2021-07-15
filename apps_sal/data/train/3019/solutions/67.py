def str_count(strng, letter):
    total = 0
    for i in range(len(strng)):
        if letter == strng[i]:
            total += 1
    return total
