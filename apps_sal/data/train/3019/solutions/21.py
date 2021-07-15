def str_count(strng, letter):
    c = 0
    for char in strng:
        if letter == char:
            c+=1
    return c
