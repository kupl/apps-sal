def str_count(strng, letter):
    strn = 0
    for i in strng:
        a = i.count(letter)
        strn += a
    return strn
