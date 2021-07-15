def str_count(strng, letter):
    val = 0
    for alpha in strng:
        if letter == alpha:
            val += 1
    print(val)
    return val

