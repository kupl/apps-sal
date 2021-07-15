def str_count(strng, letter):
    counter = 0
    for char in strng:
        if letter==char:
            counter +=1
    return counter
