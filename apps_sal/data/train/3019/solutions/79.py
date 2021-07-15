def str_count(strng, letter):
    instances = 0
    for char in strng:
        if char == letter:
            instances += 1
    return instances
