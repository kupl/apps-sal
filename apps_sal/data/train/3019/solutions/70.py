def str_count(strng, letter):

    if letter not in strng:
        return 0
    else:
        return 1 + str_count(strng.replace(letter, "", 1), letter)
