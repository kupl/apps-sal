def str_count(strng, letter):
    soln = 0
    for char in strng:
        if char == letter:
            soln += 1
    return soln
