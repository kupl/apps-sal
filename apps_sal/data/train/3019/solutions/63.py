def str_count(strng, letter):
    for i in strng:
        if strng.count(letter) >= 0:
            return strng.count(letter)
