def str_count(strng, letter):
    count = 0
    x = 0
    while x < len(strng):
        if letter == strng[x]:
            count += 1
        x += 1
    return count
