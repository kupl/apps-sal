def str_count(strng, letter):
    if strng.find(letter) == -1:
        return 0
    else:
        return strng.count(letter)
